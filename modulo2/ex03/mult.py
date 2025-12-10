#!/usr/bin/env python3

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

result = number_1 * number_2

message = "The result is "
if result < 0:
    message += "negative."
elif result > 0:
    message += "positive."
elif result == 0:
    message += "positive and negative."

print(f" {number_1} x {number_2} = {result}")
print(message)