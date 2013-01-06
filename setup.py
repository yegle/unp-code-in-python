#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

from setuptools import setup, find_packages

setup(
    name='unp',
    version='0.0.1',
    description='Unix Network Programming code in Python',
    author='yegle',
    url='https://github.com/yegle/unp-code-in-python',
    platforms='any',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'unp = unp.main:command',
        ]
    }
)
