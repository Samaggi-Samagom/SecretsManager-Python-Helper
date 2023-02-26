from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='SecretsManagerInterface',
   version='1.0.3',
   description='Python Interface to Streamline Access to SecretsManager secrets.',
   long_description=long_description,
   author='Pakkapol Lailert',
   author_email='booklailert@gmail.com',
   packages=['SecretsManagerInterface'],
   install_requires=['boto3'],
)