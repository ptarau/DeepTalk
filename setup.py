import subprocess
from sys import platform
import os
from setuptools import setup

# if __name__ == '__main__':
#

#     RELEASE_VERSION = True
#
#     if not RELEASE_VERSION:
#         # Append incremental version number from git
#         try:
#             version += (
#                 ".dev"
#                 + subprocess.check_output(["git", "rev-list", "--count", "HEAD"])
#                 .decode()
#                 .strip()
#             )
#             print(f'version = {version}')
#         except (subprocess.CalledProcessError, FileNotFoundError):
#             # The .git directory has been removed (likely by setup.py sdist),
#             # and/or git is not installed
#             version += ".dev0"
#             print(f'version = {version}')
with open('requirements.txt') as f:
    required = f.read().splitlines()
with open("README.md","r") as f:
    long_description = f.read()

version = "0.0.4"
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
  install_requires = required,
  zip_safe=False
  )
