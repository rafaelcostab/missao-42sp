#!/usr/bin/env python3

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

def average(_class):
    sum_notes = 0
    for note in _class.items():
        sum_notes += note[1]
    
    return sum_notes / len(_class)
 
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")