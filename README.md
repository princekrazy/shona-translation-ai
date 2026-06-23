---

#  BACKEND README (FastAPI)

# Shona AI Translator (Backend)

A FastAPI backend that powers an AI-based English → Shona translation system.  
It integrates translation services and stores user interactions in a database.

---

##  Live API

https://shona-translation-ai.onrender.com

---

##  Features

- REST API for translation
- Translation history storage (SQLite)
- Feedback-ready architecture
- CORS enabled for frontend integration
- Clean modular FastAPI structure

---

##  Tech Stack

- FastAPI
- Python
- SQLAlchemy
- SQLite
- deep-translator (Google Translate wrapper)

---

##  API Endpoints

### Translate text


POST /translate

Request:

{
  "text": "Hello, how are you?"
}

Response:

{
  "id": 1,
  "original": "Hello, how are you?",
  "translation": "Mhoroi, makadini"
}
Get history
GET /history

Returns list of past translations.

Architecture
Frontend (Next.js)
        ↓
FastAPI Backend
        ↓
Translation Service (Google Translate via deep_translator)
        ↓
SQLite Database
 Run Locally
1. Create virtual environment
python -m venv venv
venv\Scripts\activate
2. Install dependencies
pip install -r requirements.txt
3. Start server
uvicorn main:app --reload

Server runs on:
http://127.0.0.1:8000

Requirements
fastapi
uvicorn
sqlalchemy
pydantic
deep-translator
CORS Setup

Frontend is allowed via:

CORSMiddleware(
    allow_origins=["*"]
)
 Author

Prince (you)
Full Stack Developer | AI Enthusiast
