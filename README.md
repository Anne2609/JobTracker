# JobTracker — aplicație web pentru gestionarea candidaturilor

**Proiect individual** realizat cu Flask, HTML, CSS, JavaScript, Bootstrap și SQLite. Aplicația permite unui utilizator autentificat să urmărească firmele la care a aplicat, candidaturile, etapele de recrutare și interviurile, precum și să consulte statistici și să exporte datele.

## Funcționalități implementate

- Înregistrare, login și logout; parole stocate sub formă de hash prin Werkzeug; sesiuni prin Flask-Login.
- Candidaturi: creare, listare, căutare, filtrare după status, editare și ștergere.
- Companii: creare, listare, căutare, editare și ștergere. Ștergerea este blocată dacă există candidaturi asociate.
- Interviuri: creare, listare, editare și ștergere; interviurile aparțin unei candidaturi.
- Dashboard: total candidaturi, interviuri, oferte și candidaturi recente.
- Statistici: totaluri, rate orientative, distribuția după status și aplicările din ultimele șase luni, reprezentate cu Chart.js.
- Exportul candidaturilor utilizatorului conectat în CSV cu codificare UTF-8.
- Protecție CSRF pentru formularele POST și controlul accesului la înregistrările individuale.
- Interfață responsive cu Bootstrap 5.3.3.

## Tehnologii

| Componentă | Tehnologie |
|---|---|
| Backend | Python 3, Flask |
| ORM și baza de date | Flask-SQLAlchemy, SQLite |
| Autentificare | Flask-Login, Werkzeug |
| Frontend | HTML5 / Jinja2, CSS3, JavaScript |
| Responsive | Bootstrap 5.3.3 (CDN) |
| Grafice | Chart.js (CDN) |
| Versionare | Git / GitHub (de configurat pe calculatorul studentului) |

## Instalare și rulare pe Windows / PowerShell

1. Deschide PowerShell în directorul în care se află `app.py` și `requirements.txt`.
2. Creează un mediu virtual. Dacă Python este disponibil prin comanda `python`:

```powershell
python -m venv .venv
```

Dacă folosești instalarea existentă Radioconda (conform configurării locale discutate):

```powershell
& "C:\Users\User\radioconda\python.exe" -m venv .venv
```

3. Instalează dependențele și pornește serverul:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

4. Deschide `http://127.0.0.1:5000/register`, creează un cont și folosește aplicația.

**Important:** Baza locală apare în `instance/jobtracker.db`. Folderul `instance/` este exclus din Git pentru a nu publica datele utilizatorilor. Creează o copie de siguranță înainte de orice actualizare. Nu copia `.venv` peste un mediu deja funcțional.

### Opțional: folosirea datelor demonstrative vechi

Pentru cei care au date în contul demonstrativ creat la migrarea din etapa 4, există comanda locală `claim-legacy`. Execut-o numai după ce ai creat un cont nou și ai făcut backup al bazei de date:

```powershell
.\.venv\Scripts\python.exe -m flask --app app claim-legacy --email "ADRESA_TA_DE_EMAIL"
```

Această comandă transferă datele contului demo către contul specificat; nu o rula pe o bază partajată fără verificarea identității și a datelor.

## Structură

```text
JobTracker/
├── app.py                         # rute, validări, autentificare, rapoarte
├── models.py                      # modelele User, Company, Application, Interview
├── requirements.txt
├── templates/                     # paginile Jinja2
├── static/css/style.css
├── static/js/main.js
├── static/js/statistics.js
├── docs/
│   ├── arhitectura.md
│   ├── diagrama_bazei_de_date.md
│   ├── jurnal_ai.md
│   ├── teste_si_sustinere.md
│   └── github.md
└── .gitignore
```

## Ecrane și rute principale

| Rută | Rol |
|---|---|
| `/register`, `/login` | cont nou, autentificare |
| `/` | Dashboard |
| `/applications` | lista candidaturilor; căutare și filtrare |
| `/applications/new` | adăugare candidatură |
| `/companies` | gestionarea companiilor |
| `/interviews` | gestionarea interviurilor |
| `/statistics` | statistici și grafice |
| `/applications/export.csv` | exportul personal CSV |

Pentru editare și ștergere există rute pe identificator; ștergerile sunt operații POST. Mai multe detalii în `docs/arhitectura.md`.

## Modelul de date

Patru tabele: `users`, `companies`, `applications`, `interviews`. Fiecare companie și candidatură are un utilizator proprietar; fiecare candidatură indică o companie, iar fiecare interviu indică o candidatură. Vezi `docs/diagrama_bazei_de_date.md`.

## Verificări

Testarea manuală a etapelor 3, 5 și 6 a fost confirmată în conversația de dezvoltare de către utilizator. Pentru etapa 4 a fost confirmată funcționarea paginilor, nu este disponibilă în acest pachet o dovadă automată pentru toate cazurile CRUD. Un plan de verificare finală este în `docs/teste_si_sustinere.md`. Nu există un raport de teste automate care să justifice afirmarea unei acoperiri complete.

## Limitări cunoscute

- Serverul rulează în `debug=True` pentru dezvoltare locală; **nu** este configurat pentru producție.
- Cheia secretă are o valoare implicită doar pentru dezvoltare; setează variabila `JOBTRACKER_SECRET_KEY` cu o valoare aleatorie înainte de orice mediu partajat.
- Bootstrap și Chart.js sunt încărcate din CDN, deci pot necesita Internet.
- „Rata răspunsurilor” este o aproximare derivată din statusuri, nu detectează emailuri reale.
- Nu există confirmare automată a interviurilor prin email și nici integrare Calendar în versiunea curentă.
- Actualizările simple de schemă sunt gestionate în cod; pentru un proiect de producție ar fi preferabile migrări versionate.

## GitHub și AI

Instrucțiunile pentru crearea repository-ului și pentru **minimum cinci commit-uri reale** sunt în `docs/github.md`. Jurnalul asistenței AI și verificările efectuate sunt în `docs/jurnal_ai.md`. Nu este inclusă nicio afirmație că repository-ul sau commit-urile au fost publicate deja.
