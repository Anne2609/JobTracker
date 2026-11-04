# Testare finală și pregătire pentru susținere

## Matrice de testare manuală

Bifează după testarea **pe calculatorul propriu**; acestea sunt criterii de verificare, nu rezultate automate.

- [ ] Deschid `/register`; introduc date invalide și verific mesajul de eroare.
- [ ] Înregistrez un cont A, mă deconectez și mă conectez din nou.
- [ ] Accesez fără login `/statistics` și verific redirecționarea la login.
- [ ] Creez, modific, filtrez și șterg o candidatură.
- [ ] Creez o companie și modific industria sau locația.
- [ ] Încerc să șterg o companie cu candidaturi: operația este refuzată.
- [ ] Creez, modific și șterg un interviu asociat unei candidaturi.
- [ ] Verific actualizarea statisticilor la schimbarea statusului.
- [ ] Export CSV: deschid fișierul în Excel și verific diacriticele și valorile.
- [ ] Creez contul B și confirm că nu văd înregistrările contului A.
- [ ] Verific interfața la lățime mică, cu meniul Bootstrap comprimat.
- [ ] Verific `git status`, `.gitignore` și minimum 5 commit-uri reale în GitHub.

## Scenariu de demonstrație (5–7 minute)

1. Prezint problema: urmărirea candidaturilor fără foi separate.
2. Demonstrez Register/Login și explic hash-ul parolei.
3. Creez o companie și o candidatură, schimb statusul și folosesc filtrul.
4. Programez un interviu; arăt relația cu candidatura.
5. Deschid Dashboard/Statistics și explic indicatorii; export un CSV.
6. Explic cele patru tabele, cheile străine și controlul accesului după utilizator.
7. Prezint README, jurnalul AI și istoricul real de commit-uri pe GitHub.

## Întrebări posibile

**De ce Flask?** Este un framework Python potrivit pentru rute, șabloane și o aplicație educațională mică.

**De ce SQLAlchemy?** Permite definirea modelelor și efectuarea interogărilor fără SQL scris manual pentru fiecare operație.

**Ce înseamnă CRUD?** Create, Read, Update, Delete — creare, afișare, modificare, ștergere.

**Ce face `ForeignKey`?** Leagă un rând de un rând dintr-un alt tabel; de exemplu `interviews.application_id` indică o candidatură.

**Cum separi datele utilizatorilor?** Interogările includ ID-ul utilizatorului autentificat, iar interviurile se filtrează prin candidatura deținută.

**De ce hash-uim parola?** Pentru a nu stoca parolele în clar; verificarea se face prin `check_password_hash`.

**Ce rol are CSRF?** Tokenul validat pe POST ajută la prevenirea trimiterii neautorizate a formularelor din alte origini.

**Cum se calculează graficele?** Flask agregă înregistrările pe status și lună; Chart.js le reprezintă în browser.

**Este proiectul pregătit pentru producție?** Nu. Rulează local cu debug și setări simplificate; ar necesita întăriri de securitate și infrastructură de deployment.

## Punctaj și ce mai trebuie verificat

Proiectul include implementări pentru elementele de structură HTML, design responsive, JavaScript, patru tabele relaționale, CRUD, autentificare și statistici. **Nota sau punctajul maxim nu pot fi garantate.** Minimum cinci commit-uri GitHub și jurnalul AI completat cu verificări reale sunt cerințe distincte, care trebuie demonstrate la susținere.
