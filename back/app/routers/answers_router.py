from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.answer_schema import AnswerRequest, AnswerResponse
from app.db import get_db
from app.services.answer_service import (
    create_answer,
    get_answer,
    get_answer_by_id,
    patch_answer_by_id,
    delete_answer_by_id,
)


router = APIRouter()


@router.post("/answers", response_model=AnswerResponse)
def create_answer_endpoint(answer: AnswerRequest, db: Session = Depends(get_db)):
    """
    새로운 과목 정보를 생성하는 엔드포인트

    Args:
        answer (AnswerRequest): 생성할 과목의 요청 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerResponse: 생성된 과목의 정보
    """
    new_answer = create_answer(db, answer)
    return new_answer


@router.get("/answers", response_model=List[AnswerResponse])
def get_answer_endpoint(db: Session = Depends(get_db)):
    """
    모든 과목 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        List[AnswerResponse]: 과목 정보 리스트
    """
    answers = get_answer(db)
    return answers


@router.get("/answers/{id}", response_model=AnswerResponse)
def get_answer_by_id_endpoint(answer_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 조회하는 엔드포인트

    Args:
        answer_id (int): 조회할 과목의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerResponse: 조회된 과목의 정보
    """
    answer = get_answer_by_id(db, answer_id)
    return answer


@router.patch("/answers/{id}", response_model=AnswerResponse)
def patch_answer_by_id_endpoint(answer_id: int, patch_answer: AnswerRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 수정하는 엔드포인트

    Args:
        answer_id (int): 수정할 과목의 고유 ID
        patch_answer (AnswerRequest): 수정할 과목의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerResponse: 수정된 과목의 정보
    """
    patch_answer = patch_answer_by_id(db, answer_id, patch_answer)
    return patch_answer


@router.delete("/answers/{id}", response_model=AnswerResponse)
def delete_answer_by_id_endpoint(answer_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 삭제하는 엔드포인트

    Args:
        answer_id (int): 삭제할 과목의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerResponse: 삭제된 과목의 정보
    """
    delete_answer = delete_answer_by_id(db, answer_id)
    return delete_answer
