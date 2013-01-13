#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import os
import logging


def sig_chld(signo, ignored):
    pid, exit_status = os.wait()
    logging.warning("child %d terminated, exit_status %d" % (pid, exit_status))
