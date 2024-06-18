from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_reqiurements(file_path:str)->List[str]:
    '''
    this will return the list of reqiurements 
    '''
    reqiurements = []
    with open(file_path) as file_obj:
        reqiurements = file_obj.readlines()
        reqiurements = [req.replace('\n','') for req in reqiurements]

        if HYPEN_E_DOT in reqiurements:
            reqiurements.remove(HYPEN_E_DOT)

    return reqiurements


setup(
    name='mlproject',
    version='0.0.1',
    author ='hiransha',
    author_email='hiransham5600@gmail.com',
    packages=find_packages(),
    install_reqiures=get_reqiurements('reqiurements.txt')
)
