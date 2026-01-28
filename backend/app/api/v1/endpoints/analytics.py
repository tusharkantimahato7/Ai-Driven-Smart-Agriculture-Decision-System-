# app/api/api_v1/endpoints/analytics.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List

router = APIRouter()

@router.get("/", summary="Get analytics data")
def get_analytics():
    return {"message": "Analytics data"}
