from setuptools import setup

with open("requirements.txt", "r") as requirements:
    required_packages = [line.strip() for line in requirements.readlines()]

setup(
   name='adventofcode',
   version='0.0.1',
   description='Advent of code 2019',
   author='Łukasz Marek',
   author_email='marek.lucas@gmail.com',
   packages=['adventofcode'],  #same as name
   install_requires=required_packages #external packages as dependencies
)