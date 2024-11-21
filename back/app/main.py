from fastapi import FastAPI
from app.db import engine, Base
from app.routers import subjects_router, exams_router, questions_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(subjects_router.router, tags=["subject"])
app.include_router(exams_router.router, tags=["exam"])
app.include_router(questions_router.router, tags=["question"])
