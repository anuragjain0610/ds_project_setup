from setuptools import find_packages, setup


def get_requirements(file_path):
    """
    Function to return list of requirements to run the module
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements if '-e .' not in req]
    return requirements


setup(
    name='ds_project_setup',
    author='Anurag Jain',
    author_email='anuragjain0610@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)