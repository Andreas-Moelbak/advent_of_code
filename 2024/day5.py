#!/usr/bin/env python3

from functools import cmp_to_key

with open("day5.input", "r") as file:
    data = file.read().strip().split("\n\n")
    rules = [tuple(x.split("|")) for x in data[0].split("\n")]
    updates = [x.split(",") for x in data[1].split("\n")]


part1 = 0
incorect_updates = []
for update in updates:
    count = 0
    for i, page in enumerate(update):
        if i < len(update) - 1:
            pair = (update[i], update[i+1])
            if pair in rules:
                count += 1
    if count == len(update) - 1:
        part1 += int(update[len(update)//2])
    else:
        incorect_updates.append(update)

print("part1: ", part1)


def sort_updates(a, b):
    for rule in rules:
        if a == rule[0] and b == rule[1]:
            return -1
        if b == rule[0] and a == rule[1]:
            return 1


part2 = 0
for update in incorect_updates:
    update = sorted(update, key=cmp_to_key(sort_updates))
    part2 += int(update[len(update)//2])

print("part2: ", part2)
