#!/usr/bin/env python3


with open("day9.test", "r") as file:
    input = file.read().strip().split("\n")


directions = {"L": -1 + 0j, "R": 1 + 0j, "U": 1j, "D": -1j}

map = {}
start = 0+0j
head_pos = start
tail_pos = start

for ins in input:

    direction, steps = ins.split()
    steps = int(steps)
    print(ins)
    for i in range(steps):
        prev_head_pos = head_pos

        head_pos += directions[direction]
        tail_pos = prev_head_pos

        print(head_pos, tail_pos)
        print(head_pos - tail_pos)
        print()
    print('-'*10)
