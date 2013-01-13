#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import unittest
import sys
import subprocess
import random
import time
from multiprocessing import Process
from datetime import datetime, timedelta


try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO

port = random.randint(1025, 65535)

for server in ('daytimetcpsrv.py', 'daytimetcpsrvv6.py'):
    cmd = ('unp', 'run', 'intro/%s' % (server,), '', str(port))
    subprocess.Popen(cmd)

time.sleep(1)

class TestDaytimeTCPServerCli(unittest.TestCase):
    def test_ipv4_client(self):
        output = StringIO()
        old_stdout = sys.stdout
        sys.stdout = output
        from unp.intro import daytimetcpcli
        daytimetcpcli.main('test_daytimetcpcli', ['0.0.0.0', str(port)])
        sys.stdout = old_stdout
        delta = datetime.now() - datetime.strptime(
            output.getvalue(),
            '%Y-%m-%d %H:%M:%S.%f\n')
        self.assertLessEqual(delta, timedelta(seconds=1))

    def test_ipv6_client(self):
        output = StringIO()
        old_stdout = sys.stdout
        sys.stdout = output
        from unp.intro import daytimetcpcliv6
        daytimetcpcliv6.main('test_daytimetcpcliv6', ['::1', str(port)])
        sys.stdout = old_stdout
        delta = datetime.now() - datetime.strptime(
            output.getvalue(),
            '%Y-%m-%d %H:%M:%S.%f\n')
        self.assertLessEqual(delta, timedelta(seconds=1))
