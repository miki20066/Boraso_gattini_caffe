# Gattini Cafe API

API REST per la gestione di prodotti, categorie, utenti autenticati e ordini, sviluppata con Django REST Framework e autenticazione JWT tramite Simple JWT.

## Funzionalità

- Registrazione utente
- Login JWT con access e refresh token
- Endpoint protetto `/me/`
- Liste pubbliche di prodotti e categorie con filtri (anche con pagine HTML)
- CRUD protetto per prodotti e categorie
- Gestione ordini per utente autenticato
- Visibilità ordini filtrata per utente, con accesso completo per admin
- Aggiornamento stato ordine solo per admin
- Client per richieste di base e login JWT

## Tecnologie

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- HTML / JS / CSS

## Installazione

Clonare il repository e installare le dipendenze:

```bash
git clone <url-del-repository>
cd <nome-progetto>
pip install -r requirements.txt 
```

Eseguire le migration:
```bash
python manage.py makemigrations
python manage.py migrate
```
Avviare il server:
```bash
python manage.py runserver
```

## Utenti e autenticazione

L’autenticazione avviene tramite JWT.

### Login
`POST /api/auth/login/`

Restituisce:
- `access`
- `refresh`

### Refresh token
`POST /api/auth/token/refresh/`

### Registrazione
`POST /api/auth/register/`

### Dati utente autenticato
`GET /api/auth/me/`

Header richiesto:

```http
Authorization: Bearer <access_token>
```
## Endpoints disponibili

### Prodotti

#### Pubblici
- `GET /api/prodotti/`  
  Lista prodotti con filtri:
  - `categoria`
  - `disponibile`
  - `search`

- `GET /api/prodotti/{id}/`  
  Dettaglio prodotto

#### Protetti JWT + admin
- `POST /api/prodotti/`  
  Crea nuovo prodotto

- `PUT /api/prodotti/{id}/`  
  Modifica prodotto

- `PATCH /api/prodotti/{id}/`  
  Aggiornamento parziale prodotto

- `DELETE /api/prodotti/{id}/`  
  Elimina prodotto


### Categorie

#### Pubbliche
- `GET /api/categorie/`  
  Lista categorie

- `GET /api/categorie/{id}/`  
  Dettaglio categoria

#### Protette JWT + admin
- `POST /api/categorie/`  
  Crea nuova categoria

- `PUT /api/categorie/{id}/`  
  Modifica categoria

- `DELETE /api/categorie/{id}/`  
  Elimina categoria


### Ordini

#### Protetti JWT
- `GET /api/ordini/`  
  Lista ordini:
  - utente normale: vede solo i propri
  - admin: vede tutti

- `POST /api/ordini/`  
  Crea nuovo ordine

- `GET /api/ordini/{id}/`  
  Dettaglio ordine

#### Protetto JWT + admin
- `PATCH /api/ordini/{id}/stato/`  
  Aggiorna stato ordine

### Note
- Nel progetto sono incluse le richieste HTTP (Django) con i dati Admin per ottenere il token JWT
- Gli esempi scritti sopra sono parte delle richieste fattibili (es: get html)

## Client Frontend

### Cosa fa
Questo è un semplice client frontend in HTML + JavaScript che comunica con una Django REST API.

Permette di:
- effettuare login (JWT)
- visualizzare prodotti
- creare ordini

I dati vengono inviati e ricevuti tramite chiamate `fetch` verso il backend.

---

### Come avviarlo

1. Avvia il backend Django
2. Avvia il frontend html:
```bash
python -m http.server 5500
```
3. Apri nel browser:
```
http://127.0.0.1:5500
```
### Note
- Il backend deve avere CORS abilitato per http://127.0.0.1:5500
- Il login restituisce un token JWT salvato in localStorage
- Le richieste autenticati usano Authorization: Bearer <token>
- Lo stile è stato generato da un'Intelligenza Artificiale

## Autore
- Nicola Creazzo