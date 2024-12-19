#!/usr/bin/env python3

import re

with open("day3.input", "r") as file:
    data = file.read().strip().replace('\n', '')


#part 1
x = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
num = [[int(z) for z in j[4:-1].split(",")] for j in x]
part1 = sum([x[0] * x[1] for x in num])


#part 2
operation = [x.split("don't()")[0] for x in data.split("do()")]
y = [re.findall(r'mul\(\d{1,3},\d{1,3}\)', x) for x in operation]
y = [x for xs in y for x in xs]
num = [[int(z) for z in j[4:-1].split(",")] for j in y]
part2 = sum([x[0] * x[1] for x in num])

print(part1)
print(part2)
