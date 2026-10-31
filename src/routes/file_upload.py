from fastapi import APIRouter, Depends, UploadFile , status
from fastapi.responses import JSONResponse
from helpers import get_settings
from controllers import DataController ,projectController
from models import ResponseStatus
import aiofiles
import logging


logger = logging.getLogger('uvicorn.error')
upload_router = APIRouter()

@upload_router.post("/file-upload/{user_id}")
async def file_upload(file: UploadFile, user_id: str, settings = Depends(get_settings)):
    
    is_valid, message = DataController().upload_file_validate(file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": message}
        )

    project_path = projectController().get_project_path(user_id=user_id)
    new_file_path = DataController().unique_file_name(file.filename, user_id)
    

    try:
        async with aiofiles.open(new_file_path, 'wb') as f:
            while content := await file.read(settings.File_Upload_Chunksize):  # Read the file in chunks
                await f.write(content)
    except Exception as e:
        logger.error(f"Error occurred while uploading file: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": ResponseStatus.File_Upload_Failure.value}
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": ResponseStatus.File_Upload_Success.value}
    )
    
    
    