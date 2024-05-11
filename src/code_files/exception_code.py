def exception_code(project_name):
    exception_code ="""import sys
from src.logger import logging

def error_message(error, error_details: sys):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message_details = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message_details

class CustomException(Exception):
    def __init__(self, error_msg, error_details: str):
        super().__init__(error_msg)
        self.error_msg = error_message(error=error_msg, error_details=error_details)

    def __str__(self):
        return self.error_msg
    """
    with open(f"{project_name}/src/exception.py", "w") as file:
        file.write(exception_code)
