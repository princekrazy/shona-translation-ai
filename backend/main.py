from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from translator import translate_text

from database import SessionLocal, engine, Base
from models import Translation, Feedback
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

class FeedbackRequest(BaseModel):
    translation_id: int
    rating: str
    suggested_translation: str = ""


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
@app.post("/feedback")
def submit_feedback(
    req: FeedbackRequest,
    db: Session = Depends(get_db)
):
    feedback = Feedback(
        translation_id=req.translation_id,
        rating=req.rating,
        suggested_translation=req.suggested_translation
    )

    db.add(feedback)
    db.commit()

    return {
        "message": "Feedback saved"
    }
@app.get("/feedback")
def get_feedback(db: Session = Depends(get_db)):
    return db.query(Feedback).all()