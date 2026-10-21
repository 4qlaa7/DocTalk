from fastapi import APIRouter
import os

base_router = APIRouter()

@base_router.get("/")
def read_root():
    return{
        "APP_NAME": os.getenv("APP_NAME"),
        "APP_VERSION": os.getenv("APP_VERSION"),
    }