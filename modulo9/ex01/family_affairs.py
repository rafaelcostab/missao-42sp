#!/usr/bin/env python3

familia_dupont = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

def find_the_redheads(persons):
    names = dict(filter(lambda head_color: head_color[1] == "red", persons.items()))
    return list(names.keys())

print(find_the_redheads(familia_dupont))