#!/usr/bin/env python

import ast
import os
import re
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('screener/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.md') as readme_file:
    README = readme_file.read()

with open(os.path.join("requirements", "requirements.txt")) as reqs:
    REQUIREMENTS = reqs.readlines()


setup(
    name='screener',
    version=version,
    description='Stock Screener and fundamental analysis tool',
    long_description=README,
    license='MIT',
    long_description_content_type='text/markdown',
    author='D-one',
    author_email='reraaaaa@gmail.com',
    url='https://github.com/reraaaaa/rapid-api-python',
    keywords='financial,timeseries,trade',
    packages=[
        'screener',
    ],
    install_requires=REQUIREMENTS,
    setup_requires=['pytest-runner', 'flake8'],
)
