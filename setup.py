import subprocess
from sys import platform
import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()
with open("README.md","r") as f:
    long_description = f.read()

version = "0.1.2"
setup(name='deep_talk',
  version=version,
  description='DeepTalk: Python and Prolog based dialogue agent',
  long_description = long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/ptarau/DeepTalk.git',
  author='Paul Tarau, Andrea Cortis',
  author_USER_EMAIL='<paul.tarau@gmail.com>; andrea.cortis@gmail.com>',
  license='Apache',
  packages=['deep_talk'],
  package_data={'deep_talk': ['*.pro']},
  include_package_data=True,
  install_requires = required,
  zip_safe=False
  )
