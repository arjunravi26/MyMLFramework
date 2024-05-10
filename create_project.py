#!/usr/bin/env python3
import os,sys
from app_code import app_code
from setup_code import setup_code
from exception_code import exception_code
from logger_code import logger_code
from index_html import index_code


def create_project_structure(project_name):
    # Create the main project directory
    os.makedirs(project_name, exist_ok=True)

    # Create directories
    directories = ["artifacts", "templates", "src/components", "src/pipeline"]
    for directory in directories:
        os.makedirs(os.path.join(project_name, directory), exist_ok=True)

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
        open(os.path.join(project_name, file), "a").close()


def write_code(project_name):
    app_code(project_name)
    setup_code(project_name)
    exception_code(project_name)
    logger_code(project_name)
    index_code(project_name)


def create_project(project_name):
    create_project_structure(project_name)
    write_code(project_name)


create_project(sys.argv[1])
