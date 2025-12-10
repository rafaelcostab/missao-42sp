#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
array_new = []

for i in range(len(array)):
    array_new.append(array[i] + 2)

print("Original array: " + str(array))
print("New array: " + str(array_new))