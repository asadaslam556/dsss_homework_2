from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='math_quiz',
    version='3.11',
    packages=find_packages(),
    install_requires=requirements,
)