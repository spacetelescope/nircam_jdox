#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='nircam_jdox',
    version = '0.1',
    description = 'NIRCam notebooks and code for JDox',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/spacetelescope/nircam_jdox",
    author = 'STScI NIRCam Team',
    author_email = 'acanipe@stsci.edu',
    keywords = ['astronomy'],
    classifiers = ['Programming Language :: Python :: 3'],
    packages = find_packages(exclude=["examples"]),
    install_requires = [],
    include_package_data = True
    )
