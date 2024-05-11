#!/usr/bin/env python3
from create_project import CreateProjectStructure
import sys


def create_project_structure(project_name):
    obj = CreateProjectStructure(project_name)
    obj.create_project()


if __name__ == "__main__":
    create_project_structure(project_name=sys.argv[1])
