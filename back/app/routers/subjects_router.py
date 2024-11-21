from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.subject_schema import SubjectRequest, SubjectResponse
from app.db import get_db
from app.services.subject_service import create_subject


router = APIRouter()


@router.post("/subjects", response_model=SubjectResponse)
async def create_subject_endpoint(subject: SubjectRequest, db: Session = Depends(get_db)):
    new_subject = create_subject(db, subject)
    return new_subject
