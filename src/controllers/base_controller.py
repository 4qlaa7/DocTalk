from helpers import get_settings , Settings
import os
import random
import string

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()

        self.project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.project_path = os.path.join(self.project_dir, "assets/files")


    def generate_random_string(self, length: int = 10):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))