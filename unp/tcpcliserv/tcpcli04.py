#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import sys
import socket
from ..misc import constants as const
from ..misc import tools
from .tcpcli01 import parse


def main(prog, args):
    parsed_args = parse(prog, args)
    ip = parsed_args.ip

    servaddr = (ip, const.SERV_PORT)
    sockfds = list()

    for i in range(0, 5):
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        try:
            sockfd.connect(servaddr)
        except socket.error as e:
            tools.err_sys(e, msg="connect error")
        sockfds.append(sockfd)
    tools.str_cli(sys.stdin, sockfds[0])
