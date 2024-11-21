from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.question_schema import QuestionRequest, QuestionResponse
from app.db import get_db
from app.services.question_service import (
    create_question,
    get_question,
    get_question_by_id,
    patch_question_by_id,
    delete_question_by_id,
)


router = APIRouter()


@router.post("/questions", response_model=QuestionResponse)
def create_question_endpoint(question: QuestionRequest, db: Session = Depends(get_db)):
    """
    새로운 문제 정보를 생성하는 엔드포인트

    Args:
        question (QuestionRequest): 생성할 문제의 요청 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionResponse: 생성된 문제의 정보
    """
    new_question = create_question(db, question)
    return new_question


@router.get("/questions", response_model=List[QuestionResponse])
def get_question_endpoint(db: Session = Depends(get_db)):
    """
    모든 문제 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        List[QuestionResponse]: 문제 정보 리스트
    """
    questions = get_question(db)
    return questions


@router.get("/questions/{id}", response_model=QuestionResponse)
def get_question_by_id_endpoint(question_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 문제 정보를 조회하는 엔드포인트

    Args:
        question_id (int): 조회할 문제의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionResponse: 조회된 문제의 정보
    """
    question = get_question_by_id(db, question_id)
    return question


@router.patch("/questions/{id}", response_model=QuestionResponse)
def patch_question_by_id_endpoint(question_id: int, patch_question: QuestionRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 문제 정보를 수정하는 엔드포인트

    Args:
        question_id (int): 수정할 문제의 고유 ID
        patch_question (QuestionRequest): 수정할 문제의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionResponse: 수정된 문제의 정보
    """
    patch_question = patch_question_by_id(db, question_id, patch_question)
    return patch_question


@router.delete("/questions/{id}", response_model=QuestionResponse)
def delete_question_by_id_endpoint(question_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 문제 정보를 삭제하는 엔드포인트

    Args:
        question_id (int): 삭제할 문제의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionResponse: 삭제된 문제의 정보
    """
    delete_question = delete_question_by_id(db, question_id)
    return delete_question
