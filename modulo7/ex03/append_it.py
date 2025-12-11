#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
    exit()

sys.argv.pop(0)

for parameter in sys.argv:
    # assim funciona
    #if parameter.find("ism") != -1:
    # mas achei melhor assim
    if "ism" in parameter:
        continue;
    else:
        print(parameter + "ism")