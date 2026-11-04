# Arhitectura aplicației JobTracker

## Problema și obiective

O persoană care aplică la mai multe locuri de muncă are nevoie să păstreze într-un singur loc informațiile despre angajatori, poziții, statusurile recrutării și datele interviurilor. JobTracker oferă o evidență structurată, căutare, actualizare și o privire de ansamblu asupra progresului.

## Arhitectură

Aplicația este monolitică de tip client–server:

1. **Browser:** interpretează șabloanele HTML randate de server, CSS-ul și JavaScript-ul; Bootstrap pentru responsive; Chart.js pentru grafice.
2. **Flask (`app.py`):** gestionează rutele, metodele GET/POST, validarea pe server, CSRF, autentificarea, filtrele și exportul CSV.
3. **SQLAlchemy (`models.py`):** definește entitățile și relațiile și construiește interogările.
4. **SQLite (`instance/jobtracker.db`):** stochează înregistrările într-un fișier local ignorat de Git.

Flux tipic: browser -> request -> rută Flask -> verificare sesiune + proprietar + validare -> SQLAlchemy -> SQLite -> răspuns HTML/CSV.

## Rute, operații și reguli

| Resursă | Create | Read | Update | Delete |
|---|---|---|---|---|
| Candidaturi | `/applications/new` | `/applications` | `/applications/<id>/edit` | POST `/applications/<id>/delete` |
| Companii | `/companies/new` | `/companies` | `/companies/<id>/edit` | POST `/companies/<id>/delete` |
| Interviuri | `/interviews/new` | `/interviews` | `/interviews/<id>/edit` | POST `/interviews/<id>/delete` |

- `@login_required` protejează datele autentificate.
- Interogările pentru candidaturi/companii folosesc `current_user.id`; interviurile sunt filtrate prin candidatura deținută de utilizator.
- Formularul POST cere token CSRF păstrat în sesiune.
- Parolele sunt comparate folosind verificarea hash-urilor Werkzeug, nu sunt păstrate în clar.
- Data aplicării nu poate fi în viitor; statusurile admise sunt `Applied`, `Screening`, `Interview`, `Offer`, `Rejected`, `Withdrawn`.
- Companiile asociate candidaturilor nu pot fi șterse direct.
- La ștergerea unei candidaturi sunt șterse și interviurile asociate prin cascada ORM.

## Statistici și export

Pagina `/statistics` agregă statusuri și numărul de candidaturi pe lună (ultimele șase luni calendaristice). Rata ofertelor este `număr de candidaturi cu status Offer / total candidaturi * 100`. Rata răspunsului este estimată după status, deci nu este o metrică bazată pe emailuri. Exportul `/applications/export.csv` folosește datele utilizatorului conectat și tratează prefixele ce ar putea fi interpretate ca formule de Excel.

## Securitate și limite

Aceasta este o implementare educațională care demonstrează autentificare, autorizare la nivelul înregistrărilor, validare pe server și CSRF. Nu presupune că este pregătită pentru internet public. Pentru producție ar fi necesare configurare HTTPS, secret sigur fără fallback, limitarea încercărilor de autentificare, testare dedicată de securitate, loguri și deployment WSGI.

## Fluxul de funcționare al aplicației

Aplicația JobTracker utilizează arhitectura client-server.

**1. Frontend:** Utilizatorul interacționează cu paginile HTML, stilizate prin CSS și Bootstrap. JavaScript asigură validarea formularelor și interactivitatea.

**2. Backend:** Framework-ul Flask primește cererile HTTP, verifică autentificarea, procesează datele și execută operațiile necesare.

**3. Baza de date:** SQLite stochează informațiile despre utilizatori, companii, candidaturi și interviuri. SQLAlchemy facilitează accesul la date și gestionarea relațiilor.

**4. Securitate:** Flask-Login gestionează sesiunile utilizatorilor, iar verificările de autorizare limitează accesul la datele proprii. Formularele beneficiază de protecție CSRF.

**5. Afișarea rezultatelor:** Flask transmite informațiile către șabloanele Jinja2, care generează paginile HTML afișate în browser.