#!/usr/bin/env python3

with open("day4.input", "r") as file:
    data = file.read().strip().split("\n")



# Part 1
part1 = 0
for x in range(len(data)):
    for y in range(len(data[x])):
        if data[x][y] == "X":
            # Vertical Forward
            try:
                string = data[x][y] + data[x][y + 1] + data[x][y + 2] + data[x][y + 3]
                if string == "XMAS":
                    part1 += 1
            except:
                pass
            # Vertical Backward
            try:
                string = data[x][y] + data[x][y - 1] + data[x][y - 2] + data[x][y - 3]
                if string == "XMAS" and y >= 3:
                    part1 += 1
            except:
                pass
            # Horizontal Down
            try:
                string = data[x][y] + data[x+1][y] + data[x+2][y] + data[x+3][y]
                if string == "XMAS":
                    part1 += 1
            except:
                pass
            # Horizontal Up
            try:
                string = data[x][y] + data[x-1][y] + data[x-2][y] + data[x-3][y]
                if string == "XMAS" and x >= 3:
                    part1 += 1
            except:
                pass
            # Diagonaly Down Right
            try:
                string = data[x][y] + data[x+1][y+1] + data[x+2][y+2] + data[x+3][y+3]
                if string == "XMAS":
                    part1 += 1
            except:
                pass
            # Diagonaly Down left
            try:
                string = data[x][y] + data[x+1][y-1] + data[x+2][y-2] + data[x+3][y-3]
                if string == "XMAS" and y >= 3 :
                    part1 += 1
            except:
                pass
            # Diagonaly Up Right
            try:
                string = data[x][y] + data[x-1][y+1] + data[x-2][y+2] + data[x-3][y+3]
                if string == "XMAS" and x >= 3:
                    part1 += 1
            except:
                pass
            # Diagonaly Up left
            try:
                string = data[x][y] + data[x-1][y-1] + data[x-2][y-2] + data[x-3][y-3]
                if string == "XMAS" and y >= 3 and x >= 3:
                    part1 += 1
            except:
                pass

directions = {"digDown": ((-1, -1), (+1, +1)), "digUp": ((+1, -1), (-1, +1))}
part2 = 0
for x in range(len(data)):
    for y in range(len(data[x])):
        cur = data[x][y]
        if (
            cur == "A"
            and x > 0
            and x < len(data) - 1
            and y > 0
            and y < len(data[x]) - 1
        ):
            masCount = 0
            for dir in directions:
                xa = directions[dir][0][0]
                ya = directions[dir][0][1]
                xb = directions[dir][1][0]
                yb = directions[dir][1][1]
                string = (
                    data[x + directions[dir][0][0]][y + directions[dir][0][1]]
                    + cur
                    + data[x + directions[dir][1][0]][y + directions[dir][1][1]]
                )
                if (
                    string == "MAS"
                    or string == "SAM"
                    or string[::-1] == "MAS"
                    or string[::-1] == "SAM"
                ):
                    masCount += 1

            if masCount == 2:
                part2 += 1

print("part 1: ", part1)
print("part 2: ", part2)
