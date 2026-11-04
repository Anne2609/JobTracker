# JobTracker – Job Application Management Web Application

**Limbi / Languages:** [Română](#-română) | [English](#-english)

**GitHub Repository:** https://github.com/Anne2609/JobTracker

---

# 🇷🇴 Română

## Despre proiect

**JobTracker** este o aplicație web dezvoltată ca proiect academic individual, folosind Python, Flask, HTML, CSS, JavaScript, Bootstrap și SQLite.

Scopul aplicației este să ajute utilizatorii să gestioneze eficient candidaturile la locuri de muncă, să monitorizeze etapele de recrutare și să organizeze interviurile.

Aplicația oferă autentificare, operații CRUD, statistici interactive și posibilitatea exportării datelor în format CSV.

## Funcționalități implementate

- **Autentificare:** înregistrare, login și logout, cu parole protejate prin hashing și sesiuni Flask-Login.
- **Gestionarea candidaturilor:** adăugare, vizualizare, editare, ștergere, căutare și filtrare după status.
- **Gestionarea companiilor:** creare, afișare, modificare și ștergere, cu protejarea companiilor asociate candidaturilor.
- **Gestionarea interviurilor:** programarea, vizualizarea, modificarea și ștergerea interviurilor.
- **Dashboard:** afișarea numărului de candidaturi, interviuri și oferte.
- **Statistici:** grafice interactive cu Chart.js, distribuția candidaturilor și evoluția aplicărilor în ultimele șase luni.
- **Export CSV:** descărcarea candidaturilor utilizatorului autentificat.
- **Securitate:** validarea formularelor, protecție CSRF și acces controlat la datele utilizatorilor.
- **Design responsive:** interfață realizată cu Bootstrap 5.

## Tehnologii utilizate

| Componentă | Tehnologie |
|---|---|
| Backend | Python 3, Flask |
| Frontend | HTML5, CSS3, JavaScript, Jinja2 |
| Responsive Design | Bootstrap 5.3.3 |
| Bază de date | SQLite |
| ORM | Flask-SQLAlchemy |
| Autentificare | Flask-Login, Werkzeug |
| Grafice | Chart.js |
| Versionare | Git și GitHub |

## Instalare și rulare

**1. Clonează repository-ul:**

```powershell
git clone https://github.com/Anne2609/JobTracker.git
cd JobTracker
```

**2. Creează mediul virtual:**

```powershell
python -m venv .venv
```

Dacă Python este disponibil printr-o altă instalare, utilizează calea executabilului corespunzător.

**3. Instalează dependențele:**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**4. Pornește aplicația:**

```powershell
.\.venv\Scripts\python.exe app.py
```

**5. Accesează aplicația:**

http://127.0.0.1:5000/register

Creează un cont și autentifică-te pentru a utiliza funcționalitățile JobTracker.

## Structura proiectului

```text
JobTracker/
├── app.py
├── models.py
├── requirements.txt
├── templates/
├── static/
│   ├── css/
│   └── js/
├── docs/
│   ├── arhitectura.md
│   ├── diagrama_bazei_de_date.md
│   ├── jurnal_ai.md
│   ├── teste_si_sustinere.md
│   └── github.md
├── README.md
└── .gitignore
```

## Baza de date

Aplicația utilizează patru tabele principale:

| Tabel | Descriere |
|---|---|
| Users | Informații despre utilizatori și autentificare |
| Companies | Datele companiilor |
| Applications | Candidaturi și statusurile acestora |
| Interviews | Interviuri asociate candidaturilor |

Relațiile dintre tabele permit asocierea candidaturilor cu utilizatorii și companiile, precum și asocierea interviurilor cu candidaturile.

Diagrama bazei de date este disponibilă în `docs/diagrama_bazei_de_date.md`.

## Rute principale

| Rută | Funcționalitate |
|---|---|
| `/register` | Înregistrare |
| `/login` | Autentificare |
| `/` | Dashboard |
| `/applications` | Gestionarea candidaturilor |
| `/applications/new` | Adăugare candidatură |
| `/companies` | Gestionarea companiilor |
| `/interviews` | Gestionarea interviurilor |
| `/statistics` | Statistici și grafice |
| `/applications/export.csv` | Export CSV |

## Testare

Aplicația a fost verificată manual în timpul dezvoltării, inclusiv operațiile CRUD pentru candidaturi, autentificarea și funcționalitățile de statistici și export.

Testele automate și acoperirea completă a cazurilor de utilizare nu sunt confirmate.

## Limitări

- Aplicația este configurată pentru dezvoltare locală, nu pentru producție.
- Bootstrap și Chart.js utilizează resurse CDN.
- Rata răspunsurilor este calculată orientativ pe baza statusurilor candidaturilor.
- Nu există integrare automată cu emailul sau calendarul.
- Pentru utilizarea într-un mediu public sunt necesare configurări suplimentare de securitate.

## Utilizarea inteligenței artificiale

Inteligența artificială a fost utilizată ca instrument de asistență pentru generarea codului, depanare, structurarea documentației și verificarea logicii aplicației.

Funcționalitățile au fost testate manual în etapele de dezvoltare, iar problemele identificate au fost corectate.

Detalii suplimentare sunt disponibile în `docs/jurnal_ai.md`.

## Repository GitHub

Codul sursă este publicat la:

https://github.com/Anne2609/JobTracker

---

# 🇬🇧 English

## About the Project

**JobTracker** is a web application developed as an individual academic project using Python, Flask, HTML, CSS, JavaScript, Bootstrap, and SQLite.

The application's main purpose is to help users efficiently manage job applications, track recruitment stages, and organize interviews.

It provides user authentication, CRUD operations, interactive statistics, and CSV data export.

## Implemented Features

- **User Authentication:** registration, login, and logout with securely hashed passwords and Flask-Login sessions.
- **Job Application Management:** create, read, update, delete, search, and filter job applications.
- **Company Management:** create, view, edit, and delete companies, with safeguards for companies associated with existing applications.
- **Interview Management:** schedule, view, update, and delete interviews.
- **Dashboard:** overview of job applications, interviews, and received offers.
- **Statistics:** interactive Chart.js visualizations showing application status distribution and application trends over the last six months.
- **CSV Export:** export application data belonging to the authenticated user.
- **Security:** form validation, CSRF protection, and access control for user data.
- **Responsive Design:** Bootstrap 5 interface adapted to different screen sizes.

## Technologies Used

| Component | Technology |
|---|---|
| Backend | Python 3, Flask |
| Frontend | HTML5, CSS3, JavaScript, Jinja2 |
| Responsive Design | Bootstrap 5.3.3 |
| Database | SQLite |
| ORM | Flask-SQLAlchemy |
| Authentication | Flask-Login, Werkzeug |
| Charts | Chart.js |
| Version Control | Git and GitHub |

## Installation and Setup

**1. Clone the repository:**

```powershell
git clone https://github.com/Anne2609/JobTracker.git
cd JobTracker
```

**2. Create a virtual environment:**

```powershell
python -m venv .venv
```

If Python is installed in a different location, use the appropriate executable path.

**3. Install dependencies:**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**4. Run the application:**

```powershell
.\.venv\Scripts\python.exe app.py
```

**5. Open the application:**

http://127.0.0.1:5000/register

Create an account and log in to access the JobTracker features.

## Project Structure

```text
JobTracker/
├── app.py
├── models.py
├── requirements.txt
├── templates/
├── static/
│   ├── css/
│   └── js/
├── docs/
│   ├── arhitectura.md
│   ├── diagrama_bazei_de_date.md
│   ├── jurnal_ai.md
│   ├── teste_si_sustinere.md
│   └── github.md
├── README.md
└── .gitignore
```

## Database Architecture

The application uses four main database tables:

| Table | Description |
|---|---|
| Users | User accounts and authentication information |
| Companies | Company information |
| Applications | Job applications and recruitment statuses |
| Interviews | Interviews associated with applications |

Relationships connect applications to users and companies, while interviews are associated with specific applications.

The database diagram is available in `docs/diagrama_bazei_de_date.md`.

## Main Routes

| Route | Description |
|---|---|
| `/register` | User registration |
| `/login` | User login |
| `/` | Dashboard |
| `/applications` | Job application management |
| `/applications/new` | Create a new application |
| `/companies` | Company management |
| `/interviews` | Interview management |
| `/statistics` | Statistics and charts |
| `/applications/export.csv` | CSV data export |

## Testing

The application has undergone manual testing during development, including job application CRUD operations, authentication, statistics, and CSV export.

Automated test coverage and complete verification of all possible scenarios have not been established.

## Known Limitations

- The application is configured for local development rather than production deployment.
- Bootstrap and Chart.js depend on external CDN resources.
- Response rates are estimated from application statuses.
- Automated email and calendar integrations are not implemented.
- Additional security configuration is necessary before public deployment.

## Artificial Intelligence Usage

Artificial intelligence was used as an assistance tool for code generation, debugging, documentation, and application logic review.

Features were manually tested throughout development, and identified issues were corrected.

Further information is available in `docs/jurnal_ai.md`.

## GitHub Repository

The project's source code is publicly available at:

https://github.com/Anne2609/JobTracker

---

**JobTracker – Academic Web Development Project**

*Developed using Python, Flask, SQLite, HTML, CSS, JavaScript, and Bootstrap.*