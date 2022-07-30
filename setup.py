from setuptools import find_packages, setup

PACKAGE_NAME = 'atshop'
VERSION = '1.0.0'

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author='iclapcheeks',
    python_requires='~=3.7',
    author_email='iclapcheeeeeks@protonmail.com',
    description='A Python wrapper for the Atshop API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iclapcheeks/Atshop',
    packages=find_packages(),
    install_requires=[
        'websocket_client>=1.3.3'
    ]
)
