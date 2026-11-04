# Publicarea pe GitHub — pași de urmat

**Important:** Acest pachet nu conține un repository Git inițializat și nu au fost create/publicate commit-uri în numele studentului. Cerința cursului cere **minimum 5 commit-uri relevante reale**.

## 1. Verifică Git

Deschide PowerShell în folderul care conține `app.py`:

```powershell
git --version
```

Dacă Git lipsește, instalează-l de pe https://git-scm.com/downloads/win și redeschide PowerShell.

## 2. Inițializează și verifică ce se publică

```powershell
git init
git status
git check-ignore instance/jobtracker.db
```

Ultima comandă ar trebui să afișeze calea fișierului `.db` dacă există, confirmând excluderea lui. Nu încărca `.venv`, `instance`, `.env`, parole sau baze de date personale.

## 3. Commit inițial (versiunea finală curentă)

```powershell
git add .gitignore README.md app.py models.py requirements.txt templates static docs
git commit -m "docs: documenteaza versiunea functionala JobTracker"
```

**Nu fabrica istoricul proiectului:** dacă abia acum inițializezi Git, acesta este un singur commit. Cerința de minimum 5 commit-uri nu poate fi îndeplinită legitim prin declararea unor etape istorice neînregistrate. Continuă cu modificări reale, distincte, făcute și testate după acest moment.

## 4. Exemplu de plan pentru următoarele commit-uri reale

1. `test: adauga verificari automate pentru acces si CRUD` — după ce chiar creezi și rulezi testele.
2. `fix: imbunatateste validarea formularelor` — după ce implementezi o îmbunătățire.
3. `style: rafineaza afisarea pe mobil` — după o schimbare CSS verificată.
4. `docs: adauga capturi si rezultate reale ale testelor` — după realizarea și introducerea lor.

Pentru fiecare schimbare verifică `git diff`, apoi:

```powershell
git add .
git commit -m "descrierea modificarii efectuate"
```

Nu repeta comenzi de commit dacă nu există modificări reale.

## 5. Publică repository-ul

Creează în GitHub un repository gol numit `JobTracker` (fără fișiere inițiale) și copiază adresa sa HTTPS. Înlocuiește URL-ul exemplu **cu URL-ul real** furnizat de GitHub:

```powershell
git branch -M main
git remote add origin https://github.com/UTILIZATOR/JobTracker.git
git push -u origin main
```

Verifică pe GitHub că fișierele sunt vizibile și că pagina **Commits** afișează cel puțin cinci commit-uri reale. Dacă Git solicită autentificare, urmează fluxul oficial din browser; nu introduce parola contului în cod.
