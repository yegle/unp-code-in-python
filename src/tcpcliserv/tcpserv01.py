#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import os
import sys
import socket
sys.path.append('..')
from misc import constants as const
from misc import tools

if __name__ == '__main__':
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    # empty string means INADDR_ANY
    servaddr = ('', const.SERV_PORT)

    listenfd.bind(servaddr)
    listenfd.listen(const.LISTENQ)

    while True:
        connfd, remote_addr = listenfd.accept()

        # XXX:
        # there's a bug in this code but I cannot figure out
        # after the client disconnects, the child process still exists
        # hope someone can fix my code
        if not os.fork():
            # close listen fd in child process
            # not actual close, just minus its reference count
            # by one
            listenfd.close()
            tools.str_echo(connfd)
            connfd.close()
            sys.exit(0)

        connfd.close()
