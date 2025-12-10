#!/usr/bin/env python3

input_str = input("Por favor, me diga sua idade: ")

age = int(input_str)

print("Voce tem atualmente " + input_str + " anos de idade.")

i = 1
sum_age = 10
while i <= 3:
    print(f"Em {sum_age} anos, voce tera {age + sum_age} anos de idade.")
    sum_age += 10
    i += 1