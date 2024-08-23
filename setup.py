from setuptools import setup,find_packages
from typing import List
# Initialising the metadata of the package using setup

def find_requirements(path:str)-> List[str]:
    requirements = []
    HYPEN_DOT = '-e .'
    with open(path, 'r') as file_obj:
        for line in file_obj:
            if line.strip() != HYPEN_DOT:
                requirements.append(line.strip())
    return requirements

setup(
    name='Mlops',
    version = '0.0.1',
    author = 'Divya Sree',
    author_email= 'Divyareddy.pulipati@gmail.com',
    install_requires= find_requirements('./Requirements.txt'),
    packages=find_packages()
)