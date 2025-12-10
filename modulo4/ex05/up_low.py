#!/usr/bin/env python3

input_str = input()

invert_case = ""
for character in input_str:
    if character.isupper():
        invert_case += character.lower()
    elif character.islower():
        invert_case += character.upper()
    else:
        invert_case += character

print(invert_case)