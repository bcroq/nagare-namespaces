#!/bin/env python

# --
# Copyright (c) 2008-2013 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

VERSION = '0.1.0'

from setuptools import setup, find_packages

setup(
    name='nagare-namespaces',
    version=VERSION,
    author='Alain Poirier',
    author_email='alain.poirier at net-ng.com',
    description='Nagare Python web framework - namespaces',
    license='BSD',
    url='http://www.nagare.org',
    download_url='http://www.nagare.org/download',
    packages=find_packages(),
    namespace_packages=('nagare.namespaces', ),
    dependency_links=('http://www.nagare.org/download/',),
    install_requires=('PEAK-Rules', 'lxml>=3.0.1'),
    extras_require={
        'test': ('nose',)
    },
    test_suite='nose.collector'
)
