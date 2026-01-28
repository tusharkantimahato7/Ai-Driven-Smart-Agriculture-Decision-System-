# app/api/api_v1/endpoints/auth.py
from fastapi import APIRouter , Depends, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Authentication"])


class LoginRequest(BaseModel):
    username: str
    password: str
    
@router.post("/Login")
def login(data: LoginRequest)
if data.username == "admin" and data.password == "secret":
        return {"message": "Login successful"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, details="invalid credentials")