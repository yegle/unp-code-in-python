#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import sys
import socket
import argparse
from ..misc import constants as const
from ..misc import tools

def parse(prog, args):
    parser = argparse.ArgumentParser(prog=prog)
    parser.add_argument('ip')
    return parser.parse_args(args)

def main(prog, args):
    parsed_args = parse(prog, args)
    ip = parsed_args.ip

    servaddr = (ip, const.SERV_PORT)

    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    try:
        sockfd.connect(servaddr)
    except socket.error as e:
        tools.err_sys(e, msg="connect error")
    tools.str_cli(sys.stdin, sockfd)
