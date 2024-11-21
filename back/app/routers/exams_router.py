from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.exam_schema import ExamRequest, ExamResponse
from app.db import get_db
from app.services.exam_service import (
    create_exam,
    get_exam,
    get_exam_by_id,
    patch_exam_by_id,
    delete_exam_by_id,
)


router = APIRouter()


@router.post("/exams", response_model=ExamResponse)
def create_exam_endpoint(exam: ExamRequest, db: Session = Depends(get_db)):
    """
    새로운 과목 정보를 생성하는 엔드포인트

    Args:
        exam (ExamRequest): 생성할 과목의 요청 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamResponse: 생성된 과목의 정보
    """
    new_exam = create_exam(db, exam)
    return new_exam


@router.get("/exams", response_model=List[ExamResponse])
def get_exam_endpoint(db: Session = Depends(get_db)):
    """
    모든 과목 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        List[ExamResponse]: 과목 정보 리스트
    """
    exams = get_exam(db)
    return exams


@router.get("/exams/{id}", response_model=ExamResponse)
def get_exam_by_id_endpoint(exam_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 조회하는 엔드포인트

    Args:
        exam_id (int): 조회할 과목의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamResponse: 조회된 과목의 정보
    """
    exam = get_exam_by_id(db, exam_id)
    return exam


@router.patch("/exams/{id}", response_model=ExamResponse)
def patch_exam_by_id_endpoint(exam_id: int, patch_exam: ExamRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 수정하는 엔드포인트

    Args:
        exam_id (int): 수정할 과목의 고유 ID
        patch_exam (ExamRequest): 수정할 과목의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamResponse: 수정된 과목의 정보
    """
    patch_exam = patch_exam_by_id(db, exam_id, patch_exam)
    return patch_exam


@router.delete("/exams/{id}", response_model=ExamResponse)
def delete_exam_by_id_endpoint(exam_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 삭제하는 엔드포인트

    Args:
        exam_id (int): 삭제할 과목의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamResponse: 삭제된 과목의 정보
    """
    delete_exam = delete_exam_by_id(db, exam_id)
    return delete_exam
