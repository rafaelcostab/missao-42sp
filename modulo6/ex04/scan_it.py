#!/usr/bin/env python3

import sys


if len(sys.argv) != 3:
    print("none")
    exit()

search_string = sys.argv[1]
text = sys.argv[2]

counter = text.count(search_string)

if counter > 1:
    print(counter)
else:
    print("none")