
from sqlalchemy import Column, Integer, String, Float, Text
from backend.app.db import Base


class Tender(Base):
    __tablename__ = "tenders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    organization = Column(String(255), nullable=True)
    estimated_value = Column(Float, nullable=True)
    location = Column(String(255), nullable=True)
    deadline = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
