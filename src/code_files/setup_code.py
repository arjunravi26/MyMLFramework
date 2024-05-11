def setup_code(project_name):
    setup_code = """from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="your_project_name",
    version="0.0.1",
    author="your_name",
    author_email="your_email",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
# Replace "your_project_name", "your_name", and "your_email" with your actual project name, your name, and your email 
"""
    with open(f"{project_name}/setup.py", "w") as file:
        file.write(setup_code)
