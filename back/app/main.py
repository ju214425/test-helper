from fastapi import FastAPI
from app.db import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)
