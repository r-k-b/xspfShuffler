#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Robert K. Bell',
    'url': 'URL to get it at.',
    'download_url': 'https://github.com/InsurrectionistIllness/xspfShuffler',
    'author_email': 'rtzarius@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'}

setup(**config)

