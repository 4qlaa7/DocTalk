from .base_controller import BaseController
import os

class projectController(BaseController):
    def __init__(self):
        super().__init__()

    def get_project_path(self, user_id: str):

        project_path = os.path.join(self.project_path, user_id)
        if not os.path.exists(project_path):
            os.makedirs(project_path)
            
        return project_path