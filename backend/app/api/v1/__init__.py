# app/main.py
from fastapi import FastAPI
from app.api.api_v1.api import api_router

app = FastAPI(title="My API", version="1.0")

# Mount v1 API
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to the API"}
