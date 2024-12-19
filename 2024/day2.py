#!/usr/bin/env python3


with open("./day2.input", "r") as f:
    data = [[int(y) for y in x.split()] for x in f.read().strip().split("\n")]


part1 = 0
part2 = 0

for i in data:
    inc = set([i[j] - i[j + 1] for j in range(len(i) - 1)])
    if inc <= {1, 2, 3} or inc <= {-1, -2, -3}:
        part1 += 1

    else:
        x = [i[: j - 1] + i[j:] for j in range(1, len(i) + 1)]
        for y in x:
            inc = set([y[j] - y[j + 1] for j in range(len(y) - 1)])
            if inc <= {1, 2, 3} or inc <= {-1, -2, -3}:
                part2 += 1
                break

print(part1)
print(part1 + part2)
