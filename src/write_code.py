from src.code_files.app_code import app_code
from src.code_files.setup_code import setup_code
from src.code_files.exception_code import exception_code
from src.code_files.logger_code import logger_code
from src.code_files.index_html import index_code


def write_code(project_name):
    # to write code in the files
    app_code(project_name)
    setup_code(project_name)
    exception_code(project_name)
    logger_code(project_name)
    index_code(project_name)
