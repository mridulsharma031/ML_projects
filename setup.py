from setuptools import setup, find_packages

from typing import List

'''
below function will get all the requirements from the requirements file and install it by passing it to the setup function as install_requirements
'''
def get_requirements(filepath:str)->List[str]:
    
        requirements=[]
        hyphen_e="-e ."
        with open(filepath) as file_obj:
            requirement=file_obj.readline()
            requirements=[requirement.replace("\n","") for req in requirement]

            if hyphen_e in requirements:
                requirements.remove(hyphen_e)
        return requirements
    

setup(

    name="ML_projects",
    version='0.0.1',
    author='Mridul',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

)