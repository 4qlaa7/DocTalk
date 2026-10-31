from fastapi import APIRouter
from helpers import get_settings

base_router = APIRouter()

@base_router.get("/")
async def welcome():
    return{
        "APP_NAME": get_settings().APP_NAME,
        "APP_VERSION": get_settings().APP_VERSION,
    }