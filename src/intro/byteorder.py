#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import struct
import platform

if __name__ == '__main__':
    print(platform.platform(), end=': ')

    # We use the same idea in the original C code to detect the endian
    # of the system
    # For more information, refer to document of the struct module
    b = struct.pack('h', 0x0102)

    if (b[0], b[1]) == (1,2):
        print('big-endian')
    elif (b[0], b[1]) == (2,1):
        print('little-endian')
    else:
        print('unknown')
