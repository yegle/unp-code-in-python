#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)


import unittest
import sys
from unp.intro.byteorder import main

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO

class TestByteorder(unittest.TestCase):
    def test_byteorder_script(self):
        output = StringIO()
        old_stdout = sys.stdout
        sys.stdout = output
        main(None, None)
        sys.stdout = old_stdout

        self.assertIn(output.getvalue().split(':')[-1].strip(), ['big-endian', 'little-endian'])
