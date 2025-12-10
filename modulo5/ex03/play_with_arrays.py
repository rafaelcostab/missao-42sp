#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
array_new = []

for i in range(len(array)):
    if array[i] > 5:
        array_new.append(array[i] + 2)

array_set = set(array_new)

print(str(array))
print(str(array_set))