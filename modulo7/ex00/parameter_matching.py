#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
    exit()

parameter = sys.argv[1]

input_str = input("What was the parameter? ")

if parameter == input_str:
    print("Good Job!")
else:
    print("Nope, sorry..")