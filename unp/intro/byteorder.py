#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import struct
import platform

def main(prog, args):
    print(platform.platform(), end=': ')

    # We use the same idea in the original C code to detect the endian
    # of the system
    # For more information, refer to document of the struct module
    b = struct.pack(b'h', 0x0102)

    if b == b'\x01\x02':
        print('big-endian')
    elif b == b'\x02\x01':
        print('little-endian')
    else:
        print('unknown')

if __name__ == '__main__':
    main(None, None)
