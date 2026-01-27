from fastapi import APIRouter 
from .endpoints import analytics, auth, users, reports

api_v1_router = APIRouter()


#include each end point router 
api_v1_router.include_router(analytics.router,prefix="/anylytics", tags=["Analytics"])
api_v1_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_v1_router.include_router(crops.router,prefix="/crops", tags=["Crops"])
api_v1_router.include_router(farms.router, prefix="/farms", tags=["crops"])
api_v1_router.include_router(health.router, prefix="/health", tags=["health"])
api_v1_router.include_router(predictions.router, prefix="/predictions", tags= ["predictions"])
api_v1_router.include_router(users.router, prefix="/users", tags= ["Users"])
api_v1_router.include_router(weather.router, prefix="/prefix", tags=["weather"])
