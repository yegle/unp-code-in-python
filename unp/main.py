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

    def run(self):
        target = self.args.target
        if target.endswith('.py') or target.endswith('.c'):
            name = '.'.join(target.split('.')[:-1]).replace('/','.')
        else:
            name = target.replace('/', '.')

        name = '%s.%s' % ('unp', name)
        main = import_module(name, package='unp').main

        prog = '%s %s %s' % (os.path.basename(sys.argv[0]),
                             self.args.operation, self.args.target)
        main(prog, self.args.args)

    def show(self):
        target = self.args.target
        print('Show: %s' % (target,))
        print(self.args)

    def edit(self):
        pass

command = UNPCommand()
