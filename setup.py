# coding: utf-8

"""CONS3RT Python SDK

Python client library for interacting with the API in CONS3RT-powered environments.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

NAME = 'cons3rt'
VERSION = '1.0.2'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ['urllib3 >= 1.15', 'six >= 1.10', 'certifi', 'python-dateutil']

setup(
    name=NAME,
    version=VERSION,
    description='CONS3RT Python SDK',
    url='https://api.cons3rt.com/',
    author='Jackpine Technologies Corp.',
    author_email='support@jackpinetech.com',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='cons3rt cloud orchestration devops devsecops security',
    packages=find_packages(exclude=['test', 'tests']),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=REQUIRES
)
