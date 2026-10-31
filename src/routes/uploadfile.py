from fastapi import APIRouter, Depends, UploadFile
from helpers import get_settings

upload_router = APIRouter()

@upload_router.get("/file-upload")
async def file_upload(file: UploadFile, settings = Depends(get_settings)):
    
    allowed_types = settings.File_ALLOWED_TYPES
    if file.content_type not in allowed_types:
        return {"error": f"File type '{file.content_type}' is not allowed."}

    # Check if the file size exceeds the maximum limit
    max_size_mb = settings.MAX_File_Upload_Size_MB
    max_size_bytes = max_size_mb * 1024 * 1024
    file_size = await file.read()
    if len(file_size) > max_size_bytes:
        return {"error": f"File size exceeds the maximum limit of {max_size_mb} MB."}

    return {"message": "File uploaded successfully."}