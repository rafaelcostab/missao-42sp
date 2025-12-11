#!/bin/bash

./scan_it.py | cat -e

./scan_it.py "the" | cat -e

./scan_it.py "the" "hello world" | cat -e

./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e