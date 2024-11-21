from fastapi import FastAPI
from app.db import engine, Base
from app.routers import subjects_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(subjects_router.router, tags=["subject"])
