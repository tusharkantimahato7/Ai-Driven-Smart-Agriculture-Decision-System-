from fastapi import APIRouter 
from .endpoints import analytics, auth, users, reports

api_v1_router = APIRouter()


#include each end point router 
api_v1_router.include_router(analytics.router,prefix="/anylytics", tags=["Analytics"])