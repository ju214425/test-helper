from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from app.db import Base


class Exam(Base):
    __tablename__ = "exams"

    exam_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer, ForeignKey("subjects.subject_id"), nullable=False)
    name = Column(String(100), nullable=False)

    subject = relationship("Subject", back_populates="exams")
    questions = relationship("Question", back_populates="exam")
