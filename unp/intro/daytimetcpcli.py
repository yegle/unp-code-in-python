#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import sys
import os
import socket
import argparse

from ..misc import constants as const
from ..misc import tools


def parse(prog, args):
    parser = argparse.ArgumentParser(prog=prog)
    parser.add_argument('ip')
    parser.add_argument('port', default=13, type=int)
    return parser.parse_args(args)


def main(prog, args):
    parsed_args = parse(prog, args)

    address = (parsed_args.ip, parsed_args.port)

    # Creating a socket
    # same like the assignment to sockfd
    # in the original C code
    # I didn't wrap it with try-except because
    # I don't know what exception will be raised here
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    try:
        sockfd.connect(address)
    except socket.error as e:
        tools.err_sys(e, msg='connection error')

    line = sockfd.recv(const.MAXLINE)

    print(line)
