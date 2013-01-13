#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import unittest
import sys
import subprocess
import random
import time
import os
import signal
from multiprocessing import Process
from datetime import datetime, timedelta


try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO



class TestDaytimeTCPV4(unittest.TestCase):
    def setUp(self):
        self.port = random.randint(1025, 65535)
        cmd = ('unp', 'run', 'intro/daytimetcpsrvv6.py', '', str(self.port))
        self.server_pid = subprocess.Popen(cmd).pid
        time.sleep(1)

    def tearDown(self):
        os.kill(self.server_pid, signal.SIGTERM)

    def test_ipv6_client(self):
        output = StringIO()
        old_stdout = sys.stdout
        sys.stdout = output
        from unp.intro import daytimetcpcliv6
        daytimetcpcliv6.main('test_daytimetcpcliv6', ['::1', str(self.port)])
        sys.stdout = old_stdout
        delta = datetime.now() - datetime.strptime(
            output.getvalue(),
            '%Y-%m-%d %H:%M:%S.%f\n')
        self.assertLessEqual(delta, timedelta(seconds=1))
