from .base_controller import BaseController
from fastapi import UploadFile
from models import ResponseStatus
import re
import os


class DataController(BaseController):
    def __init__(self):
        super().__init__()


    def upload_file_validate(self, file: UploadFile):
        allowed_types = self.app_settings.File_ALLOWED_TYPES

        if file.content_type not in allowed_types:
            return False, ResponseStatus.File_Type_Not_Allowed.value

        if file.size> self.app_settings.File_MAX_Upload_Size_MB * 1024 * 1024:
            return False, ResponseStatus.File_Size_Exceeds_Limit.value

        return True, ResponseStatus.File_Upload_Success.value

    def unique_file_name(self, file_name: str, user_id: str):
        project_path = os.path.join(self.project_path, user_id)
        random_string = self.generate_random_string()
        cleaned_file_name = self.get_cleaned_file_name(file_name)
        unique_file_name = os.path.join(random_string + "_" + cleaned_file_name)
        

        new_file_path = os.path.join(project_path, unique_file_name)

        while os.path.exists(new_file_path):
            random_string = self.generate_random_string()
            unique_file_name = os.path.join(random_string + "_" + cleaned_file_name)
            new_file_path = os.path.join(project_path, unique_file_name)

        return new_file_path

    

    def get_cleaned_file_name(self, file_name: str):
        # Remove special characters and spaces from the file name
        cleaned_file_name = re.sub(r'[^a-zA-Z0-9_.-]', '', file_name)
        return cleaned_file_name