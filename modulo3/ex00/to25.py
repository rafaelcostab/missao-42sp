#!/usr/bin/env python3

input_str = input("Enter a number less than 25: ")

number = int(input_str)

if number > 25:
    print("Error")
    exit()

i = number
while i <= 25:
    print("Inside the loop, my variable is " + str(i))
    i +=1
