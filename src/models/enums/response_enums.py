from enum import Enum

class ResponseStatus(Enum):
    File_Upload_Success = "File uploaded successfully."
    File_Upload_Failure = "File upload failed." 
    File_Type_Not_Allowed = "File type not allowed."
    File_Size_Exceeds_Limit = "File size exceeds the maximum limit."
    