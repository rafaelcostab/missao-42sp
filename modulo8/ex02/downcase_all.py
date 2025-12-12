#!/usr/bin/env python3

import sys

def downcase_it(value):
    return str(value).lower()

if len(sys.argv) == 1:
    print("none")
    exit()

sys.argv.pop(0)
for param in sys.argv:
    print(downcase_it(param))