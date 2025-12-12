#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
    exit()

sys.argv.pop(0)

params = sys.argv

if int(params[0]) >= int(params[1]):
    exit()

array = []

for num in range(int(params[0]), (int(params[1])+1)):
    array.append(num)

print(array)