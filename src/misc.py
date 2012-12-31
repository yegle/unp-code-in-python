#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import logging
import sys

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
