#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import sys
import socket
from ..misc import constants as const
from ..misc import tools

from .daytimetcpcli import parse

def main(prog, args):
    parsed_args = parse(prog, args)
    ip = parsed_args.ip

    # This is an AF_INET6 address defination
    address = (ip, 13)

    # Creating a socket
    # same like the assignment to sockfd
    # in the original C code
    sockfd = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)

    try:
        sockfd.connect(address)
    except socket.error as e:
        tools.err_sys(e, msg='connection error')

    line = sockfd.recv(const.MAXLINE)

    print(line)
