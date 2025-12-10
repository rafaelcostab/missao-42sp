#!/usr/bin/env python3

import sys

if len(sys.argv) > 2:
    for arg in reversed(sys.argv):
        print(arg)
else:
    print("none")