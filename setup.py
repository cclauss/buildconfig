# -*- coding: utf8 -*-

from setuptools import setup, find_packages
import sys

packages = find_packages()
if sys.version_info.major < 3:
    packages.pop('buildconfig.yaml._yaml3', None)
else:
    packages.pop('buildconfig.yaml._yaml2', None)

setup(
    name        = 'buildconfig',
    packages    = packages,
    scripts     = ['bin/buildconfig'],
    package_data= {
        '': ['runpersistent/*.sh']
    },
    include_package_data=True,
    version     = '0.4',
    description = '.buildconfig edit build integration tool',
    author      = 'Moritz Möller',
    author_email= 'mm@mxs.de',
    url         = 'https://github.com/mo22/buildconfig'
)
