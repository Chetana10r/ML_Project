from setuptools import find_packages,setup
from typing import List

HyPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for re in requirements]

        if HyPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='ML_Project',
version='0.0.1',
author='Chetana',
author_email='chetanarane10@gmail.com',
packages=find_packages(),
install_requires=get_requirements['requirement.txt']

)