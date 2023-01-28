#!/usr/bin/env python3

from collections import defaultdict
from os import wait
import re

with open("day7.input", "r") as file:
    data = file.read().strip().split("\n")


def add_path_to_dir(path, directory):
    if path not in directory.keys():
        directory[path] = 0
    return directory


curent_path = ''
current_stack = []
directories_size = {}

for line in data:
    if line.startswith("$ cd"):
        if not line.startswith("$ cd ..") and not line.startswith("$ cd /"):
            curent_path += f"/{line.split()[-1]}" if curent_path != "/" else line.split()[-1]
            current_stack.append(curent_path)
            directories_size = add_path_to_dir(curent_path, directories_size)

        elif line.strip() == "$ cd /":
            curent_path = "/"
            current_stack = ["/"]
            directories_size = add_path_to_dir(curent_path, directories_size)

        elif line.strip() == "$ cd ..":
            curent_path = "/".join(curent_path.split("/")[:-1])
            current_stack.pop()
            
    if line[0].isdigit():
        file_size = int(line.split()[0])
        for directory in current_stack:
            directories_size[directory] += file_size

liste = [el for el in directories_size.values() if el <= 100000]
print("Part One: ", sum(liste))

target_space = 30000000
total_space = 70000000
curently_used_space = directories_size["/"]

free_space = total_space - curently_used_space
liste = [el for el in directories_size.values() if el+free_space >= target_space]
liste.sort()
print("Part Two: ", liste[0])

