#!/usr/bin/env python3

pessoas = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

def array_de_nomes(persons):
    array = []
    for person in persons.items():
        array.append(str(person[0]).capitalize() + " " + str(person[1]).capitalize())

    return array

print(array_de_nomes(pessoas))