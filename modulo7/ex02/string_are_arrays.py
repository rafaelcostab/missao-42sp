#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
    exit()

parameter = sys.argv[1]
counter_character = 0

for character in parameter:
    if character == "z":
        print("z", end="")
        counter_character += 1

if counter_character == 0:
    print("none")
else: 
    print()