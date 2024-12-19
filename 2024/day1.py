#!/usr/bin/env python3

with open("day1.input", "r") as file:
    data = file.read().strip().split("\n")

x = []
y = []
for i in data:
    a, b = i.split()
    x.append(int(a))
    y.append(int(b))

x.sort()
y.sort()

distance = 0
similarity = 0
for i, j in zip(x, y):
    distance += max(i, j) - min(i, j)
    similarity += i * y.count(i)


print("distance : ", distance)
print("similarity : ", similarity)
