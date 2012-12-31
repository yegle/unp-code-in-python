#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import sys
import socket
from misc import *

if __name__ == '__main__':
    if len(sys.argv) !=2:
        err_quit('usage: %s <IPAddress>' % (sys.argv[0]))

    # This is an AF_INET address defination
    address = (sys.argv[1], 13)

    # Creating a socket
    # same like the assignment to sockfd
    # in the original C code
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sockfd.connect(address)
    except ConnectionError as e:
        err_sys(e, msg='connection error')

    line = sockfd.recv(1024)

    print(line)
