
from fastapi import FastAPI
from pydantic import BaseModel

from backend.app.db import engine, Base, SessionLocal
from backend.app import models


# Request schema for creating a tender
class TenderCreate(BaseModel):
    title: str
    organization: str
    estimated_value: float
    location: str
    deadline: str
    description: str


# Initialize FastAPI
app = FastAPI(
    title="TenderLens API",
    description="Backend API for TenderLens tender analysis platform",
    version="1.0.0"
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to TenderLens API",
        "status": "running"
    }


# Health Check API
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "TenderLens"
    }


# Get all tenders
@app.get("/tenders")
def get_all_tenders():
    db = SessionLocal()

    try:
        tenders = db.query(models.Tender).all()

        return [
            {
                "id": tender.id,
                "title": tender.title,
                "organization": tender.organization,
                "estimated_value": tender.estimated_value,
                "location": tender.location,
                "deadline": tender.deadline,
                "description": tender.description
            }
            for tender in tenders
        ]

    finally:
        db.close()


# Create a new tender
@app.post("/tenders")
def create_tender(tender: TenderCreate):
    db = SessionLocal()

    try:
        new_tender = models.Tender(
            title=tender.title,
            organization=tender.organization,
            estimated_value=tender.estimated_value,
            location=tender.location,
            deadline=tender.deadline,
            description=tender.description
        )

        db.add(new_tender)
        db.commit()
        db.refresh(new_tender)

        return {
            "message": "Tender created successfully",
            "id": new_tender.id,
            "title": new_tender.title,
            "organization": new_tender.organization,
            "estimated_value": new_tender.estimated_value,
            "location": new_tender.location,
            "deadline": new_tender.deadline,
            "description": new_tender.description
        }

    finally:
        db.close()
