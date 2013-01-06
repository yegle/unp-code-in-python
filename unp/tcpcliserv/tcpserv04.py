#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import os
import sys
import socket
import signal
import errno
from ..misc import constants as const
from ..misc import tools
from .sigchldwaitpid import sig_chld

def main(prog, args):
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    # empty string means INADDR_ANY
    servaddr = ('', const.SERV_PORT)

    listenfd.bind(servaddr)
    listenfd.listen(const.LISTENQ)

    signal.signal(signal.SIGCHLD, sig_chld)

    while True:
        try:
            connfd, remote_addr = listenfd.accept()
        except socket.error as e:
            if e.errno == errno.EINTR:
                continue
            else:
                tools.err_sys(e, msg="accept error")

        if not os.fork():
            # close listen fd in child process
            # not actual close, just minus its reference count
            # by one
            listenfd.close()
            tools.str_echo(connfd)
            connfd.close()
            sys.exit(0)

        connfd.close()
