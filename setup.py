from setuptools import find_packages,setup
from typing import List

def get_requirements(text)->List[str]:
    with open(text,'r') as f:
        requirement = f.readlines()
        requirements = [req.strip() for req in requirement]
    if '-e.' in requirements:requirements.remove('-e.')
    return requirements

setup(
    name = "sensor fault detection",
    version = "0.0.1",
    author = "DEV",
    author_email = "dev03@gmail.com",
    install_requirements = get_requirements("requirements.txt"),
    packages = find_packages()
)