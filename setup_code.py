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
    name="mlproject",
    version="0.0.1",
    author="Arjun",
    author_email="arjunravi1523@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

    """
    app_file_path = f"{project_name}/setup.py"
    with open(app_file_path, "w") as file:
        file.write(setup_code)
