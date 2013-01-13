#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import sys
from setuptools import setup, find_packages

if sys.version_info < (2,7):
    extra_dep = ['argparse', 'importlib']
else:
    extra_dep = []

setup(
    name='unp',
    version='0.0.1',
    description='Unix Network Programming code in Python',
    author='yegle',
    url='https://github.com/yegle/unp-code-in-python',
    platforms='any',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'unp = unp.main:command',
        ]
    },
    install_requires=[] + extra_dep
)
