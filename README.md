
🐾 Boraso Gattini Cafe API
Backend API REST per la gestione di una caffetteria felina. Sviluppato con Django + DRF, protetto da autenticazione JWT.

🚀 Quick Start
Installazione: pip install -r requirements.txt

Database: Inserire gattini_cafe.db nella root.

Avvio: python manage.py runserver

🔐 Sicurezza & Auth 
JWT (Simple JWT): Login, Refresh e registrazione.

Header: Authorization: Bearer <token>

Accesso: Pubblico (Menu), Utente (Ordini), Admin (Gestione totale).

☕ Endpoints Principali
Menu: GET /api/prodotti/ e /api/categorie/ (con filtri e ricerca).

Ordini: POST /api/ordini/ (calcolo automatico del totale).

Gestione: CRUD completo su prodotti/categorie e gestione stati ordini (Staff).

💻 Client Frontend
Incluso nella cartella /client: interfaccia HTML5/JS con Dark Theme personalizzato. Consente:

Login e salvataggio token.

Visualizzazione catalogo in tempo reale.

Invio ordinazioni direttamente al DB.