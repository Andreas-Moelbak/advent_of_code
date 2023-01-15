#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pprint import pprint

with open("day9.test", "r") as file:
    input = file.read().strip().split("\n")


directions = {"L": -1 + 0j, "R": 1 + 0j, "U": 1j, "D": -1j}

start = 0 + 0j
head_pos = start
prev_head_pos = head_pos
tail_pos = start

rope_length = 2
rope = [list() for _ in range(rope_length)]

head_trail = []
tail_trail = []
head_trail.append(head_pos)
tail_trail.append(tail_pos)


for ins in input:
    direction, steps = ins.split()
    for i in range(int(steps)):
        prev_head_pos = head_pos
        head_pos += directions[direction]

        diff = head_pos - tail_pos
        dx, dy = diff.real, diff.imag

        if abs(dx) > 1 or abs(dy) > 1:
            tail_pos = prev_head_pos

        head_trail.append(head_pos)
        tail_trail.append(tail_pos)


print(len(set(tail_trail)))
hx = [ele.real for ele in head_trail]
hy = [ele.imag for ele in head_trail]

tx = [ele.real for ele in tail_trail]
ty = [ele.imag for ele in tail_trail]

fig, ax = plt.subplots()
ax.set_xlim([-1, 8])
ax.set_ylim([-1, 8])
scat1 = ax.scatter(hx[0], hy[0])
scat2 = ax.scatter(tx[0], ty[0])


def animate(i):
    scat1.set_offsets((hx[i], hy[i]))
    scat2.set_offsets((tx[i], ty[i]))
    return scat1, scat2


ani = animation.FuncAnimation(fig, animate, repeat=True, frames=len(hx), interval=1000)
plt.show()
