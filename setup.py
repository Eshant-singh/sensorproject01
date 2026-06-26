# setup tools is basically a package where have a information of a project
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e.'

def get_requirments(file_path: str) -> List[str]:
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n", "") for req in requirments]

    if HYPHEN_E_DOT in requirments:
        requirments.remove(HYPHEN_E_DOT)
    return requirments


setup(
    name= "Fault detection",
    version= '0.0.1',
    author= 'Eshant Singh',
    author_email= 'eshant@live.com',
    install_requires= get_requirments('requirments.txt'),
    packages= find_packages() 
)