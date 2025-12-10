#!/usr/bin/env python3

table = 0
message = ""

while table <= 10:
    message += "Table of " + str(table) + ": "

    multiplier = 0
    while multiplier <= 10:
        message += str(table * multiplier) + " "
        multiplier += 1
    
    message += "\n"
    table += 1

print(message)