from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    source_text = Column(String)
    translated_text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)