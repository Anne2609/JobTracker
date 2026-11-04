# Jurnalul utilizării AI

Acest jurnal rezumă contribuțiile AI din conversația de dezvoltare. Textele de mai jos reprezintă cereri formulate sau parafrazate fidel, nu transcrieri complete ale tuturor prompturilor. Nu susțin că verificări neconfirmate au avut loc.

| Etapa | Cerere / prompt (rezumat) | Rezultat AI | Verificare / intervenție umană |
|---|---|---|---|
| 1 | Crearea JobTracker din cerințele cursului | Flask, HTML/CSS, Bootstrap, Dashboard inițial | Utilizatorul a instalat/configurat Python și a pornit Dashboard-ul în browser. |
| 2 | Conectarea bazei de date | Modele User, Company, Application, Interview și configurare SQLite | Utilizatorul a descoperit că `app.py` nu fusese actualizat; a înlocuit codul și a confirmat că etapa a fost finalizată. |
| 3 | Adăugarea CRUD pentru candidaturi | Rute și formulare pentru creare, citire, modificare, ștergere și filtre | Prima arhivă nu conținea rutele așteptate; s-a verificat `app.py`, s-a livrat o variantă corectată; utilizatorul a confirmat cinci teste CRUD. |
| 4 | Gestionarea companiilor și interviurilor | Două pagini cu CRUD și relații | Utilizatorul a confirmat existența funcțiilor `companies()` și `interviews()` și că aplicația merge; nu există în conversație confirmare separată a tuturor testelor CRUD din etapa 4. |
| 5 | Autentificare și protecția conturilor | Register/Login/Logout, Flask-Login, protecție CSRF, izolare date | Utilizatorul a confirmat trecerea tuturor celor cinci teste propuse în conversație. |
| 6 | Statistici, grafice și export CSV | Chart.js, agregări pentru șase luni și export personal | Utilizatorul a confirmat trecerea tuturor celor cinci teste propuse în conversație. |
| 7 | Pregătirea pentru GitHub și documentația finală | README, arhitectură, diagramă ER, plan de teste, jurnal AI și ghid GitHub | Documentele au fost redactate pe baza fișierelor etapei 6; publicarea repository-ului trebuie realizată de student. |

## Erori și lecții

1. **Python nu era disponibil prin `py` sau `python`**; s-a identificat instalarea Python 3.12.9 inclusă în Radioconda și s-a folosit calea directă.
2. **Proiectul se rula uneori din alt director**; o versiune nouă a arhivei nu actualizează automat fișierele proiectului. S-au folosit `Get-Content`, `Select-String` și verificarea rutei direct în browser.
3. **Baza de date nu apărea** deoarece `app.py` era în versiunea fără `db.create_all()`; problema a fost diagnosticată din conținutul real al fișierului.
4. **Arhiva etapa 3 inițială nu adusese ruta așteptată**; validarea manuală a dus la remediere.

## Ce trebuie explicat la susținere

Studentul trebuie să poată prezenta diferența dintre Flask și SQLAlchemy, rolul `ForeignKey`, verificarea `current_user.id`, funcția CSRF, hash-ul parolei, fiecare operație CRUD, mecanismul graficelor și exportul CSV. Codul AI a necesitat verificări și corecții; folosirea AI nu substituie înțelegerea implementării.
