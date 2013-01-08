#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import argparse
import os
import sys
import unp
import subprocess
from importlib import import_module

class UNPCommand(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='UNP code in Python')

        self.parse_arguments()

    def __call__(self):
        if self.args.operation == 'run':
            self.run()
        elif self.args.operation == 'show':
            self.show()
        elif self.args.operation == 'edit':
            self.edit()
        elif self.args.operation == 'ls':
            self.ls()

    def parse_arguments(self):
        self.parser.add_argument('operation', choices=['run', 'show',
                                                       'edit', 'ls'])
        self.parser.add_argument('target')
        self.parser.add_argument('args', nargs=argparse.REMAINDER)
        self.args = self.parser.parse_args()

        self.file = os.path.join(
            os.path.dirname(__file__),
            self.args.target
        )

    def get_module(self):
        target = self.args.target
        if target.endswith('.py') or target.endswith('.c'):
            module_name = '.'.join(target.split('.')[:-1]).replace('/', '.')
        else:
            module_name = target.replace('/', '.')
        return import_module('%s.%s' % ('unp', module_name), package='unp').main

    def run(self):
        prog = '%s %s %s' % (os.path.basename(sys.argv[0]),
                             self.args.operation, self.args.target)

        self.get_module()(prog, self.args.args)

    def show(self):
        print(self.file)

    def edit(self):
        editor = os.environ.get('EDITOR', None) or 'vim'
        # XXX: security problem?
        subprocess.call([editor, self.file])

    def ls(self):
        raise NotImplementedError('Please be patient, or send pull-request!')

command = UNPCommand()
