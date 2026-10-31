from fastapi import APIRouter, Depends, UploadFile
from helpers import get_settings
from controllers import DataController

upload_router = APIRouter()

@upload_router.get("/file-upload")
async def file_upload(file: UploadFile, settings = Depends(get_settings)):
    
    is_valid, message = DataController().upload_file_validate(file)
    return {
        'result': is_valid,
        'message': message
    }