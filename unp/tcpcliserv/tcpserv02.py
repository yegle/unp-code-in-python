#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import os
import sys
import socket
import signal
from ..misc import constants as const
from ..misc import tools
from .sigchldwait import sig_chld

def main(prog, args):
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    # empty string means INADDR_ANY
    servaddr = ('', const.SERV_PORT)

    listenfd.bind(servaddr)
    listenfd.listen(const.LISTENQ)

    signal.signal(signal.SIGCHLD, sig_chld)
    signal.siginterrupt(signal.SIGCHLD, False)

    while True:
        # XXX
        # In Python, socket.accept() is written in C so it will block
        # the main process from receiving the SIGCHLD signal
        # Thus the child process will remain in zombie status untill
        # next connection from client and this accept returns.
        #
        # By setting up timeout to listenfd and wrap accept in a loop is
        # a solution but not a perfect one.
        connfd, remote_addr = listenfd.accept()

        if not os.fork():
            # close listen fd in child process
            # not actual close, just minus its reference count
            # by one
            listenfd.close()
            tools.str_echo(connfd)
            connfd.close()
            sys.exit(0)

        connfd.close()
