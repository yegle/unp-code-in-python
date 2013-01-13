#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import logging
import sys
import socket
from . import constants as const


def err_quit(msg=None):
    err_do_it('ERROR', None, msg)
    sys.exit(1)


def err_sys(e, msg=None):
    err_do_it('ERROR', e, msg)
    sys.exit(1)


def err_do_it(level, e, msg):
    if e:
        text = "[Errno: %d] %s" % (e.errno, e.strerror)
        if msg:
            text += ', detail: %s' % (msg,)
    else:
        text = msg

    if level == 'WARNING':
        logging.warning(text)
    elif level == 'ERROR':
        logging.error(text)


def str_echo(fd):
    try:
        while True:
            b = fd.recv(const.MAXLINE)
            if len(b) > 0:
                fd.send(b)
            else:
                break
    except socket.error as e:
        error_sys(e, msg='str_echo read error')


def str_cli(fp, sockfd):
    while True:
        line = fp.readline(const.MAXLINE).strip()
        if not line:
            break

        sockfd.send(line.encode('utf-8'))

        recv = sockfd.recv(const.MAXLINE)
        if not recv:
            err_quit(msg='str_cli: server terminated prematurely')

        print(recv)
