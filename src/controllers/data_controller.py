from .base_controller import BaseController
from fastapi import UploadFile

class DataController(BaseController):
    def __init__(self):
        super().__init__()


    def upload_file_validate(self, file: UploadFile):
        allowed_types = self.app_settings.File_ALLOWED_TYPES

        if file.content_type not in allowed_types:
            return False,'file type not allowed'

        if file.size> self.app_settings.MAX_File_Upload_Size_MB * 1024 * 1024:
            return False, 'file size exceeds the maximum limit'

        return True, 'File uploaded successfully.'