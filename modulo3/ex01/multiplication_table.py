#!/usr/bin/env python3

input_str = input("Enter a number: ")

number = int(input_str)

i = 1
while i < 10:
    print(f"{i} x {input_str}  = {i * number}")
    i +=1
