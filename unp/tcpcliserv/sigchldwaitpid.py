#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import os
import logging
import signal

def sig_chld(signo, ignored):
    # XXX:
    # Definately some race condition happened here, haven't figured out
    # why.
    # Error message: RuntimeError: reentrant call inside
    # <_io.BufferedWriter name='<stderr>'>
    try:
        pid, exit_status = os.waitpid(-1, 0)
        logging.warning("child %d terminated, exit_status %d" % (pid,
                                                                 exit_status))
    except ChildProcessError:
        pass
