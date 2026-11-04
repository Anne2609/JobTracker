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