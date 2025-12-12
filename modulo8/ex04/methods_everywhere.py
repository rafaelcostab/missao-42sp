#!/usr/bin/env python3

import sys

def shrink(text):
    # slice "fatia" a string
    print(text[:8])

def enlarge(text):
    while len(text) < 8:
        text += 'Z'

    print(text)

sys.argv.pop(0)
if len(sys.argv) == 0:
    exit()

for param in sys.argv:
    if len(param) > 8:
        shrink(param)
    elif len(param) < 8:
        enlarge(param)
    else:
        print(param)
