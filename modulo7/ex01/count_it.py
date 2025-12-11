#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
    exit()

print(f"parameters: {len(sys.argv) - 1}")

# primeiro elemento é o nome do script precisamos removê-lo
sys.argv.pop(0)

for parameter in sys.argv:
    if parameter != "":
        print(f"{parameter}: {len(parameter)}")