#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

install_requires = [
    'agate>=1.3.0',
    'requests>=2.9.1',
    'pyyaml>=3.11',
    'pandas>=0.17.1'
]

setup(
    name = 'pandas-lookup',
    version = '0.1.0',
    description = 'pandas-lookup adds remote lookup table to pandas dataframes',
    long_description = open('README.md').read(),

    url = 'http://pandas-lookup.readthedocs.org/',

    author = 'Kris Harbold',
    author_email = 'kris.harbold@gmail.com',
    license = 'MIT',

    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python 2.7',
        'Programming Language :: Python 3.3',
        'Programming Language :: Python 3.4',
        'Programming Language :: Python 3.5',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Utilities',
    ],
    keywords = 'pandas, lookup',

    packages = find_packages(),
    install_requires = install_requires
)
