from fastapi import APIRouter, Depends, UploadFile
from helpers import get_settings

base_router = APIRouter()

@base_router.get("/welcome")
async def welcome(settings = Depends(get_settings)):
    return{
        "APP_NAME": settings.APP_NAME,
        "APP_VERSION": settings.APP_VERSION,
    }


