# app/api/api_v1/endpoints/auth.py
from fastapi import APIRouter , Depends, HTTPException, status
from pydantic import BaseModel