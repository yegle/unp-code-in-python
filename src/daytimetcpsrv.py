#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import socket
from datetime import datetime

if __name__ == '__main__':
    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    # Listen on any local IP, and port 13
    listen_addr = ('', 13)

    listenfd.bind(listen_addr)
    listenfd.listen(1)

    while True:
        connfd, remote_addr = listenfd.accept()

        # XXX: in Python, socket works with bytes
        # So this code may only work on Python3
        # since str in py3k is unicode
        now = str(datetime.now()).encode('utf-8')
        connfd.send(now)
        connfd.close()
