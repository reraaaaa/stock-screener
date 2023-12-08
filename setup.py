#!/usr/bin/env python

import ast
import os
import re
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('rapid_api/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.md') as readme_file:
    README = readme_file.read()

with open(os.path.join("requirements", "requirements.txt")) as reqs:
    REQUIREMENTS = reqs.readlines()


setup(
    name='rapid_api',
    version=version,
    description='Rapid API python client',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Rapid',
    author_email='reraaaaa@gmail.com',
    url='https://github.com/reraaaaa/rapid-api-python',
    keywords='financial,timeseries,api,trade',
    packages=[
        'rapid_api',
    ],
    install_requires=REQUIREMENTS,
    setup_requires=['pytest-runner', 'flake8'],
)
