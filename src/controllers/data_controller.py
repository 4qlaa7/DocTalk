from .base_controller import BaseController
from fastapi import UploadFile
from models import ResponseStatus

class DataController(BaseController):
    def __init__(self):
        super().__init__()


    def upload_file_validate(self, file: UploadFile):
        allowed_types = self.app_settings.File_ALLOWED_TYPES

        if file.content_type not in allowed_types:
            return False, ResponseStatus.File_Type_Not_Allowed.value

        if file.size> self.app_settings.MAX_File_Upload_Size_MB * 1024 * 1024:
            return False, ResponseStatus.File_Size_Exceeds_Limit.value

        return True, ResponseStatus.File_Upload_Success.value