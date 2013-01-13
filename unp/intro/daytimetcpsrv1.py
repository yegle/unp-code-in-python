#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import socket
import sys
import logging
from ..misc import constants as const
from datetime import datetime

def parse(prog, args):
    parser = argparse.ArgumentParser(
        prog=prog,
        description='Daytime TCP Server for IPv4, with log output',
    )
    parser.add_argument(
        'ip',
        help='IP Address to listen to. (default 0.0.0.0)',
        default='0.0.0.0',
        nargs='?'
    )
    parser.add_argument(
        'port',
        help='Port to listen to. (default 13)',
        type=int,
        default=13,
        nargs='?'
    )
    return parser.parse_args(args)

def main(prog, args):
    parsed_args = parse(prog, args)

    listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    if parsed_args.ip == '0.0.0.0':
        ip = ''

    # Listen on any local IP, and port 13
    # Note: empty address '' represents INADDR_ANY
    listen_addr = (ip, parsed_args.port)

    listenfd.bind(listen_addr)
    listenfd.listen(const.LISTENQ)

    logging.basicConfig(level=logging.INFO)

    while True:
        # This is a difference between C version of accept
        # and Python version of accept. Python will return
        # the socket object and remote address at the same
        # time
        connfd, remote_addr = listenfd.accept()
        logging.info('Connection from %s, port %s' % (
            remote_addr[0], remote_addr[1]))

        # XXX: in Python, socket works with bytes
        # So this code may only work on Python3
        # since I assume str is unicode here
        now = str(datetime.now()).encode('utf-8')
        connfd.send(now)
        connfd.close()
