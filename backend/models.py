from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from database import Base

class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    source_text = Column(String)
    translated_text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)

    translation_id = Column(Integer, ForeignKey("translations.id"))

    rating = Column(String)  # good or bad

    suggested_translation = Column(String)