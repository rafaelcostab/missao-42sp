#!/bin/bash

./string_are_arrays.py | cat -e

./string_are_arrays.py "The character Z is not found in this string" | cat -e

./string_are_arrays.py "The character z is found in this string" | cat -e

./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e

