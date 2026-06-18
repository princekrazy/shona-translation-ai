from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from translator import translate_text

from database import SessionLocal, engine, Base
from models import Translation
import models  # ensures table registration

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TranslationRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "Shona AI API running"}


@app.post("/translate")
def translate(req: TranslationRequest, db: Session = Depends(get_db)):
    translated = translate_text(req.text)

    record = Translation(
        source_text=req.text,
        translated_text=translated
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "id": record.id,
        "original": req.text,
        "translation": translated,
        "source_lang": "en",
        "target_lang": "sn"
    }


@app.get("/history")
def history(db: Session = Depends(get_db)):
    results = db.query(Translation).order_by(Translation.id.desc()).all()

    return [
        {
            "id": r.id,
            "original": r.source_text,
            "translation": r.translated_text,
            "created_at": r.created_at
        }
        for r in results
    ]