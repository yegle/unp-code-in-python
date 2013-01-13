#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import sys
from ..misc import constants as const
from ..misc import tools
import socket


def str_echo(fd):
    try:
        while True:
            b = fd.recv(const.MAXLINE)
            if len(b) > 0:
                u = b.decode('utf-8')
                arg1, arg2 = u.split(' ')
                ret = "%s" % (int(arg1) + int(arg2))
                fd.send(ret.encode('utf-8'))
            else:
                fd.send('input error\n'.encode('utf-8'))
    except socket.error as e:
        tools.error_sys(e, msg='str_echo read error')
