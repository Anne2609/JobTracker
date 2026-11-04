# Jurnal AI – Etapa 5

**Solicitare:** Adăugarea autentificării la proiectul JobTracker existent, fără pierderea bazei de date.

**Rezultat:** Flask-Login, parole hash-uite, rute register/login/logout, filtrarea CRUD și a statisticilor după utilizator, formular cu protecție CSRF, compatibilitate cu schema din etapa 4.

**Verificări necesare:** test înregistrare, autentificare, logout, refuz acces neautentificat, imposibilitatea accesării candidaturilor celuilalt cont și verificarea datelor vechi după migrare.

**Observație:** Orice cod generat cu AI este analizat și verificat înainte de prezentarea proiectului.

## Etapa 6 – asistență AI
Prompt: „Continuăm cu etapa 6: statistici, grafice și export CSV.”
Propunere: pagină protejată `/statistics`, grafice Chart.js și export CSV doar pentru datele utilizatorului.
Verificare: se vor testa accesul autentificat, separarea pe utilizatori, corectitudinea numărătorilor, caracterele CSV și rezultatele în Excel.
