#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import argparse
import os
import sys
import unp
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

    def parse_arguments(self):
        self.parser.add_argument('operation', choices=['run', 'show',
                                                       'edit'])
        self.parser.add_argument('target')
        self.parser.add_argument('args', nargs=argparse.REMAINDER)
        self.args = self.parser.parse_args()

        self.file = os.path.join(
            os.path.dirname(__file__),
            self.args.target
        )

        target = self.args.target
        if target.endswith('.py') or target.endswith('.c'):
            module_name = '.'.join(target.split('.')[:-1]).replace('/', '.')
        else:
            module_name = target.replace('/', '.')
        self.main = import_module('%s.%s' % ('unp', module_name), package='unp').main

    def run(self):
        prog = '%s %s %s' % (os.path.basename(sys.argv[0]),
                             self.args.operation, self.args.target)
        self.main(prog, self.args.args)

    def show(self):
        print(self.file)

    def edit(self):
        pass

command = UNPCommand()
