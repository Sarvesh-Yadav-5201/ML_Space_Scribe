from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path : str) -> List[str]:
    '''
    This particular function returns the list of requirements:

    '''
    requiremetns = []
    with open(file_path) as file_obj:
        requiremetns = file_obj.readlines()
        requiremetns = [req.replace('\n','') for req in requiremetns]

        if '-e .' in requiremetns:
            requiremetns.remove('-e .')
    return requiremetns


setup(
    name = 'ai_space_scribe',
    version = '0.0.1',
    author = 'Sarvesh',
    author_email= 'sarveshkyadav.5201@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')

)