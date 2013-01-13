#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import os
import sys
import socket
from ..misc import constants as const
from ..misc import tools


def main(prog, args):
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    # empty string means INADDR_ANY
    servaddr = ('', const.SERV_PORT)

    listenfd.bind(servaddr)
    listenfd.listen(const.LISTENQ)

    while True:
        connfd, remote_addr = listenfd.accept()

        # XXX:
        # There's a bug in this code that it doesn't handle the exit of
        # child process. Upon child process exit, this process will
        # become a zombie process. UNP is aware of this problem and
        # there's another example that fixes this problem
        if not os.fork():
            # close listen fd in child process
            # not actual close, just minus its reference count
            # by one
            listenfd.close()
            tools.str_echo(connfd)
            connfd.close()
            sys.exit(0)

        connfd.close()
