#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import sys
import socket
sys.path.append('..')
from misc import constants as const
from misc import tools

if __name__ == '__main__':
    try:
        ip = sys.argv[1]
    except IndexError:
        tools.err_quit(msg="usage: %s <IPAddress>" % (sys.argv[0],))

    servaddr = (ip, const.SERV_PORT)

    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    try:
        sockfd.connect(servaddr)
    except socket.error as e:
        tools.err_sys(e, msg="connect error")
    tools.str_cli(sys.stdin, sockfd)
