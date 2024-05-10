def setup_code(project_name):
    setup_code = """from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list the requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="your_project_name",
    version="0.0.1",
    author="your_name",
    author_email="your_email",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
# Replace your_project_name with the actual name of your project, your_name with your real name,
# and your_email with your valid email address.


    """
    app_file_path = f"{project_name}/setup.py"
    with open(app_file_path, "w") as file:
        file.write(setup_code)
