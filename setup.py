#!/usr/bin/env python3

"""Setup script"""

from setuptools import setup, find_packages

setup(
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['test']),
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=([
        'osc_lib',
        'python-openstackclient',
    ]),
)
