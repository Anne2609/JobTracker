"""JobTracker - etapa 5: autentificare și date private pe utilizator."""
import os
import secrets
import csv
import io
import click
from collections import Counter
from datetime import date, timedelta
from flask import Flask, abort, flash, redirect, render_template, request, session, url_for, Response
from sqlalchemy import or_, func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from sqlalchemy import inspect, text
from models import db, User, Company, Application, Interview

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Autentifică-te pentru a continua."
login_manager.login_message_category = "warning"

@login_manager.user_loader
def load_user(user_id):
    try:
        return db.session.get(User, int(user_id))
    except (ValueError, TypeError):
        return None

STATUSES = ("Applied", "Screening", "Interview", "Offer", "Rejected", "Withdrawn")

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.environ.get('JOBTRACKER_SECRET_KEY', 'local-dev-only-change-before-deployment'),
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
        SQLALCHEMY_DATABASE_URI='sqlite:///jobtracker.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if test_config:
        app.config.update(test_config)
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Migrarea simplă a bazei vechi (etapa 4). Se păstrează datele.
        inspector = inspect(db.engine)
        if 'companies' in inspector.get_table_names():
            columns = {column['name'] for column in inspector.get_columns('companies')}
            if 'user_id' not in columns:
                with db.engine.begin() as connection:
                    connection.execute(text('ALTER TABLE companies ADD COLUMN user_id INTEGER'))
                    connection.execute(text('UPDATE companies SET user_id = 1 WHERE user_id IS NULL'))
        db.create_all()
        # Contul demo vechi este păstrat doar ca să nu dispară datele existente.
        if db.session.get(User, 1) is None:
            demo = User(name='Demo local', email='demo@jobtracker.local',
                        password_hash=generate_password_hash(secrets.token_urlsafe(32)))
            db.session.add(demo)
            db.session.commit()
        # Asigură proprietarul companiilor deja existente din etapa 4.
        with db.engine.begin() as connection:
            connection.execute(text('UPDATE companies SET user_id = 1 WHERE user_id IS NULL'))

    @app.context_processor
    def shared_values():
        return dict(statuses=STATUSES)

    @app.before_request
    def csrf_protection():
        if request.method == 'POST':
            sent = request.form.get('csrf_token', '')
            expected = session.get('csrf_token', '')
            if not expected or not secrets.compare_digest(sent, expected):
                abort(400, description='Formularul a expirat. Reincarca pagina si incearca din nou.')

    @app.context_processor
    def csrf_context():
        def csrf_token():
            if 'csrf_token' not in session:
                session['csrf_token'] = secrets.token_urlsafe(32)
            return session['csrf_token']
        return dict(csrf_token=csrf_token)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        if request.method == 'POST':
            name = request.form.get('name', '').strip()
            email = request.form.get('email', '').strip().lower()
            password = request.form.get('password', '')
            confirm = request.form.get('confirm_password', '')
            if not name or len(name) > 100:
                flash('Numele trebuie să aibă 1–100 de caractere.', 'danger')
            elif not email or len(email) > 255 or '@' not in email or email.startswith('@') or email.endswith('@'):
                flash('Introdu o adresă de email validă.', 'danger')
            elif len(password) < 10 or len(password) > 128:
                flash('Parola trebuie să aibă între 10 și 128 de caractere.', 'danger')
            elif password != confirm:
                flash('Parolele nu coincid.', 'danger')
            elif User.query.filter(db.func.lower(User.email) == email).first():
                flash('Acest email este deja înregistrat.', 'danger')
            else:
                user = User(name=name, email=email, password_hash=generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash('Contul a fost creat. Bine ai venit!', 'success')
                return redirect(url_for('dashboard'))
        return render_template('register.html', active_page='register')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        if request.method == 'POST':
            email = request.form.get('email', '').strip().lower()
            password = request.form.get('password', '')
            user = User.query.filter(db.func.lower(User.email) == email).first()
            if user and check_password_hash(user.password_hash, password):
                login_user(user)
                flash('Autentificare reușită.', 'success')
                return redirect(url_for('dashboard'))
            flash('Email sau parolă incorecte.', 'danger')
        return render_template('login.html', active_page='login')

    @app.post('/logout')
    @login_required
    def logout():
        logout_user()
        session.clear()
        flash('Te-ai deconectat.', 'success')
        return redirect(url_for('login'))

    @app.route('/')
    @login_required
    def dashboard():
        apps = Application.query.filter_by(user_id=current_user.id)
        return render_template('dashboard.html', active_page='dashboard',
            applications_count=apps.count(),
            interviews_count=Interview.query.join(Application).filter(Application.user_id == current_user.id).count(),
            offers_count=apps.filter_by(status='Offer').count(),
            recent=apps.order_by(Application.id.desc()).limit(5).all())

    @app.route('/applications')
    @login_required
    def applications():
        term=request.args.get('q','').strip()
        status=request.args.get('status','').strip()
        query=Application.query.join(Company).filter(Application.user_id == current_user.id)
        if term:
            query=query.filter(or_(Application.position.ilike(f'%{term}%'),Company.name.ilike(f'%{term}%')))
        if status in STATUSES:
            query=query.filter(Application.status == status)
        items=query.order_by(Application.applied_at.desc(),Application.id.desc()).all()
        return render_template('applications.html', active_page='applications',items=items,q=term,selected_status=status)

    def validate_form():
        position=request.form.get('position','').strip()
        company_name=request.form.get('company','').strip()
        raw_date=request.form.get('applied_at','')
        status=request.form.get('status','')
        notes=request.form.get('notes','').strip()
        if not position or len(position)>150:
            return None,'Titlul pozitiei este obligatoriu (maximum 150 de caractere).'
        if not company_name or len(company_name)>150:
            return None,'Numele companiei este obligatoriu (maximum 150 de caractere).'
        if status not in STATUSES:
            return None,'Selecteaza un status valid.'
        try:
            applied_at=date.fromisoformat(raw_date)
        except ValueError:
            return None,'Introdu o data valida.'
        if applied_at>date.today():
            return None,'Data candidaturii nu poate fi in viitor.'
        if len(notes)>5000:
            return None,'Notele sunt prea lungi (maximum 5000 de caractere).'
        return dict(position=position,company=company_name,applied_at=applied_at,status=status,notes=notes),None

    def get_or_create_company(name):
        company=Company.query.filter(Company.user_id == current_user.id, db.func.lower(Company.name)==name.lower()).first()
        if company is None:
            company=Company(name=name, user_id=current_user.id)
            db.session.add(company)
            db.session.flush()
        return company

    @app.route('/applications/new',methods=['GET','POST'])
    @login_required
    def add_application():
        if request.method=='POST':
            data,error=validate_form()
            if error:
                flash(error,'danger')
            else:
                company=get_or_create_company(data['company'])
                application=Application(user_id=current_user.id,company_id=company.id,position=data['position'],
                    status=data['status'],applied_at=data['applied_at'],notes=data['notes'])
                db.session.add(application)
                db.session.commit()
                flash('Candidatura a fost adaugata.','success')
                return redirect(url_for('applications'))
        return render_template('application_form.html',active_page='applications',item=None,today=date.today().isoformat())

    @app.route('/applications/<int:app_id>/edit',methods=['GET','POST'])
    @login_required
    def edit_application(app_id):
        item=Application.query.filter_by(id=app_id,user_id=current_user.id).first_or_404()
        if request.method=='POST':
            data,error=validate_form()
            if error:
                flash(error,'danger')
            else:
                company=get_or_create_company(data['company'])
                item.company_id=company.id
                item.position=data['position']
                item.status=data['status']
                item.applied_at=data['applied_at']
                item.notes=data['notes']
                db.session.commit()
                flash('Candidatura a fost actualizata.','success')
                return redirect(url_for('applications'))
        return render_template('application_form.html',active_page='applications',item=item,today=date.today().isoformat())

    @app.post('/applications/<int:app_id>/delete')
    @login_required
    def delete_application(app_id):
        item=Application.query.filter_by(id=app_id,user_id=current_user.id).first_or_404()
        db.session.delete(item)
        db.session.commit()
        flash('Candidatura a fost stearsa.','success')
        return redirect(url_for('applications'))


    # --- Etapa 4: gestionarea companiilor ---
    @app.route('/companies')
    @login_required
    def companies():
        term = request.args.get('q', '').strip()
        query = Company.query.filter_by(user_id=current_user.id)
        if term:
            query = query.filter(Company.name.ilike(f'%{term}%'))
        items = query.order_by(Company.name.asc()).all()
        return render_template('companies.html', active_page='companies', items=items, q=term)

    def validate_company():
        name = request.form.get('name', '').strip()
        industry = request.form.get('industry', '').strip()
        location = request.form.get('location', '').strip()
        website = request.form.get('website', '').strip()
        if not name or len(name) > 150:
            return None, 'Numele companiei este obligatoriu (maxim 150 caractere).'
        if len(industry) > 100 or len(location) > 150 or len(website) > 255:
            return None, 'Unul dintre campuri depaseste limita de caractere.'
        if website and not (website.startswith('https://') or website.startswith('http://')):
            return None, 'Website-ul trebuie sa inceapa cu https:// sau http://.'
        return dict(name=name, industry=industry, location=location, website=website), None

    @app.route('/companies/new', methods=['GET','POST'])
    @login_required
    def add_company():
        if request.method == 'POST':
            data, error = validate_company()
            if error:
                flash(error, 'danger')
            elif Company.query.filter(Company.user_id == current_user.id, db.func.lower(Company.name) == data['name'].lower()).first():
                flash('Exista deja o companie cu acest nume.', 'danger')
            else:
                db.session.add(Company(user_id=current_user.id, **data))
                db.session.commit()
                flash('Compania a fost adaugata.', 'success')
                return redirect(url_for('companies'))
        return render_template('company_form.html', active_page='companies', item=None)

    @app.route('/companies/<int:company_id>/edit', methods=['GET','POST'])
    @login_required
    def edit_company(company_id):
        item = Company.query.filter_by(id=company_id, user_id=current_user.id).first_or_404()
        if request.method == 'POST':
            data, error = validate_company()
            duplicate = Company.query.filter(
                db.func.lower(Company.name) == data['name'].lower(), Company.id != item.id, Company.user_id == current_user.id
            ).first() if data else None
            if error:
                flash(error, 'danger')
            elif duplicate:
                flash('Exista deja o companie cu acest nume.', 'danger')
            else:
                for field, value in data.items():
                    setattr(item, field, value)
                db.session.commit()
                flash('Compania a fost actualizata.', 'success')
                return redirect(url_for('companies'))
        return render_template('company_form.html', active_page='companies', item=item)

    @app.post('/companies/<int:company_id>/delete')
    @login_required
    def delete_company(company_id):
        item = Company.query.filter_by(id=company_id, user_id=current_user.id).first_or_404()
        if item.applications:
            flash('Compania nu poate fi stearsa: are candidaturi asociate. Sterge sau muta intai candidaturile.', 'danger')
        else:
            db.session.delete(item)
            db.session.commit()
            flash('Compania a fost stearsa.', 'success')
        return redirect(url_for('companies'))

    # --- Etapa 4: gestionarea interviurilor ---
    @app.route('/interviews')
    @login_required
    def interviews():
        items = (Interview.query.join(Application)
                 .filter(Application.user_id == current_user.id)
                 .order_by(Interview.scheduled_at.asc(), Interview.id.asc()).all())
        return render_template('interviews.html', active_page='interviews', items=items)

    def validate_interview():
        from datetime import datetime
        raw_application = request.form.get('application_id', '')
        raw_date = request.form.get('scheduled_at', '')
        interview_type = request.form.get('interview_type', '').strip()
        notes = request.form.get('notes', '').strip()
        try:
            application_id = int(raw_application)
            scheduled_at = datetime.fromisoformat(raw_date)
        except (ValueError, TypeError):
            return None, 'Alege candidatura si o data/ora valida.'
        application = Application.query.filter_by(id=application_id, user_id=current_user.id).first()
        if not application:
            return None, 'Candidatura aleasa nu exista.'
        if interview_type not in ('Online','Telefonic','La sediu','Altul'):
            return None, 'Alege un tip de interviu valid.'
        if len(notes) > 5000:
            return None, 'Notele depasesc 5000 de caractere.'
        return dict(application_id=application_id, scheduled_at=scheduled_at,
                    interview_type=interview_type, notes=notes), None

    @app.route('/interviews/new', methods=['GET','POST'])
    @login_required
    def add_interview():
        choices = Application.query.filter_by(user_id=current_user.id).order_by(Application.position).all()
        if request.method == 'POST':
            data, error = validate_interview()
            if error:
                flash(error, 'danger')
            else:
                db.session.add(Interview(**data))
                db.session.commit()
                flash('Interviul a fost programat.', 'success')
                return redirect(url_for('interviews'))
        return render_template('interview_form.html', active_page='interviews',
                               item=None, choices=choices)

    @app.route('/interviews/<int:interview_id>/edit', methods=['GET','POST'])
    @login_required
    def edit_interview(interview_id):
        item = (Interview.query.join(Application).filter(
            Interview.id == interview_id, Application.user_id == current_user.id).first_or_404())
        choices = Application.query.filter_by(user_id=current_user.id).order_by(Application.position).all()
        if request.method == 'POST':
            data, error = validate_interview()
            if error:
                flash(error, 'danger')
            else:
                for field, value in data.items():
                    setattr(item, field, value)
                db.session.commit()
                flash('Interviul a fost actualizat.', 'success')
                return redirect(url_for('interviews'))
        return render_template('interview_form.html', active_page='interviews',
                               item=item, choices=choices)

    @app.post('/interviews/<int:interview_id>/delete')
    @login_required
    def delete_interview(interview_id):
        item = (Interview.query.join(Application).filter(
            Interview.id == interview_id, Application.user_id == current_user.id).first_or_404())
        db.session.delete(item)
        db.session.commit()
        flash('Interviul a fost sters.', 'success')
        return redirect(url_for('interviews'))

    # --- Etapa 6: statistici si rapoarte individuale ---
    @app.get('/statistics')
    @login_required
    def statistics():
        items = (Application.query.filter_by(user_id=current_user.id)
                 .order_by(Application.applied_at.asc(), Application.id.asc()).all())
        status_counts = Counter(item.status for item in items)
        labels = list(STATUSES)
        counts = [status_counts.get(status, 0) for status in labels]

        # Ultimele sase luni calendaristice, inclusiv luna curenta.
        today = date.today()
        year, month = today.year, today.month
        month_starts = []
        for offset in range(5, -1, -1):
            total = year * 12 + (month - 1) - offset
            month_starts.append((total // 12, total % 12 + 1))
        monthly_count = Counter((item.applied_at.year, item.applied_at.month)
                                for item in items)
        month_labels = [f'{m:02d}/{y}' for y, m in month_starts]
        month_values = [monthly_count.get((y, m), 0) for y, m in month_starts]

        interviewed_application_ids = {
            application_id for (application_id,) in
            db.session.query(Interview.application_id)
              .join(Application, Interview.application_id == Application.id)
              .filter(Application.user_id == current_user.id).distinct().all()
        }
        responses = sum(item.status in ('Screening', 'Interview', 'Offer', 'Rejected')
                        for item in items)
        total = len(items)
        offers = status_counts.get('Offer', 0)
        return render_template(
            'statistics.html', active_page='statistics',
            total=total, offers=offers,
            interviews_count=(Interview.query.join(Application)
                              .filter(Application.user_id == current_user.id).count()),
            interview_application_count=len(interviewed_application_ids),
            response_rate=round(responses / total * 100, 1) if total else 0,
            offer_rate=round(offers / total * 100, 1) if total else 0,
            status_labels=labels, status_counts=counts,
            month_labels=month_labels, month_counts=month_values,
        )

    @app.get('/applications/export.csv')
    @login_required
    def export_applications():
        # Filtrarea dupa utilizator este obligatorie si la export.
        items = (Application.query.join(Company)
                 .filter(Application.user_id == current_user.id)
                 .order_by(Application.applied_at.desc(), Application.id.desc()).all())
        output = io.StringIO(newline='')
        writer = csv.writer(output)
        writer.writerow(['ID', 'Pozitie', 'Companie', 'Status', 'Data aplicarii',
                         'Industrie', 'Locatie companie', 'Website', 'Note'])
        for item in items:
            company = item.company
            # Previne executarea formulelor la deschiderea CSV in Excel/Sheets.
            def safe(value):
                value = '' if value is None else str(value)
                if value.lstrip().startswith(('=', '+', '-', '@', '\t', '\r', '\n')):
                    return "'" + value
                return value
            writer.writerow([item.id, safe(item.position), safe(company.name),
                             item.status, item.applied_at.isoformat(),
                             safe(company.industry), safe(company.location),
                             safe(company.website), safe(item.notes)])
        csv_content = '\ufeff' + output.getvalue()
        return Response(csv_content, mimetype='text/csv; charset=utf-8', headers={
            'Content-Disposition': 'attachment; filename="jobtracker_candidaturi.csv"',
            'Cache-Control': 'private, no-store',
            'X-Content-Type-Options': 'nosniff',
        })

    @app.cli.command('claim-legacy')
    @click.option('--email', required=True, help='Emailul contului nou, deja înregistrat.')
    def claim_legacy(email):
        """Mută înregistrările demo din etapa 4 în contul nou (numai local)."""
        target = User.query.filter(db.func.lower(User.email) == email.strip().lower()).first()
        demo = User.query.filter_by(email='demo@jobtracker.local').first()
        if not target or not demo or target.id == demo.id:
            raise click.ClickException('Contul nou sau contul demonstrativ nu există.')
        napps = Application.query.filter_by(user_id=demo.id).update({'user_id': target.id})
        ncompanies = Company.query.filter_by(user_id=demo.id).update({'user_id': target.id})
        db.session.commit()
        click.echo(f'Transferate {napps} candidaturi și {ncompanies} companii către {target.email}.')

    return app

app=create_app()

if __name__=='__main__':
    app.run(debug=True)
