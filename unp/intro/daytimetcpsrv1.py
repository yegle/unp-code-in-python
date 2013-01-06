#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import socket
import sys
import logging
from ..misc import constants as const
from datetime import datetime

def main(prog, args):
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    # Listen on any local IP, and port 13
    # Note: empty address '' represents INADDR_ANY
    listen_addr = ('', 13)

    listenfd.bind(listen_addr)
    listenfd.listen(const.LISTENQ)

    logging.basicConfig(level=logging.INFO)

    while True:
        # This is a difference between C version of accept
        # and Python version of accept. Python will return
        # the socket object and remote address at the same
        # time
        connfd, remote_addr = listenfd.accept()
        logging.info('Connection from %s, port %s' % (remote_addr[0],
                                                     remote_addr[1]))

        # XXX: in Python, socket works with bytes
        # So this code may only work on Python3
        # since I assume str is unicode here
        now = str(datetime.now()).encode('utf-8')
        connfd.send(now)
        connfd.close()
