import os
from src.write_code import write_code


class CreateProjectStructure:
    def __init__(self, project_name: str) -> None:
        # Create the main project directory
        self.project_name = project_name
        os.makedirs(self.project_name, exist_ok=True)

    def create_folders(self):

        # Create directories
        directories = ["artifacts", "templates", "src/components", "src/pipeline"]
        for directory in directories:
            os.makedirs(os.path.join(self.project_name, directory), exist_ok=True)

    def create_files(self):

        # Create files
        files = [
            "requirements.txt",
            "README.md",
            "app.py",
            "src/__init__.py",
            "src/logger.py",
            "src/exception.py",
            "src/utils.py",
            "templates/index.html",
            "setup.py",
        ]
        for file in files:
            open(os.path.join(self.project_name, file), "a").close()

    def write_files(self):
        # to write code in the files
        write_code(self.project_name)

    def create_project(self):
        self.create_folders()
        self.create_files()
        self.write_files()
