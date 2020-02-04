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
        'netaddr',
        'osc_lib',
        'python-openstackclient',
    ]),
    entry_points={
        'openstack.common': [
            'uos_routing_port_create=uosclient.port:CreateRoutingPort',
            'uos_routing_port_delete=uosclient.port:DeleteRoutingPort',
        ],
    },
)
