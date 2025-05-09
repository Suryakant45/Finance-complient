'''

from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "finance-complaint"
VERSION = "0.1"
AUTHOR = "Suryakant Sahoo"
DESRCIPTION = "This is a sample for industry ready solution"

REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    #name=PROJECT_NAME,
    name='Finance_project',
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(),
   # install_requires=get_requirements_list()
    install_requires=[]
)

'''

from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "finance-complaint"
VERSION = "0.1"
AUTHOR = "Suryakant Sahoo"
DESCRIPTION = "This is a sample for industry ready solution"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    with open(REQUIREMENT_FILE_NAME) as req_file:
        return [line.strip() for line in req_file if line.strip() and not line.startswith("-e")]

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
