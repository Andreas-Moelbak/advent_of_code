#!/usr/bin/env python3

from collections import Counter


with open("day6.input", "r") as file:
    data = file.read().strip()

# Part One
for idx, char in enumerate(data):
    if idx > 3:
        liste = data[idx-4:idx]
        if len(Counter(liste)) == 4:
            print(idx)
            break

# Part Two
for idx, char in enumerate(data):
    if idx > 13:
        liste = data[idx-14:idx]
        if len(Counter(liste)) == 14:
            print(idx)
            break
