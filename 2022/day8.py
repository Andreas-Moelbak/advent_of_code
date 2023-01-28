#!/usr/bin/env python3


def check_visibility(tree_height, line_of_sight):
    for tree in line_of_sight:
        if tree < tree_height:
            continue
        else:
            return False
    else:
        return True


def check_distance(tree_height, line_of_sight):
    amount = 0
    for tree in line_of_sight:
        if tree >= tree_height:
            amount += 1
            break
        else:
            amount += 1
    return amount


with open("day8.input", "r") as file:
    data = file.read().strip().split("\n")


forrest = []
for d in data:
    forrest.append([j for j in d])

visible_trees_edge = (2 * len(forrest) + 2 * len(forrest[0])) - 4
visible_trees = 0

# Part One
for y in range(1, len(forrest) - 1):
    for x in range(1, len(forrest[0]) - 1):
        tree_height = forrest[y][x]

        right = forrest[y][x + 1:]
        left = forrest[y][:x]
        top = [row[x] for idx, row in enumerate(forrest) if idx < y]
        bottom = [row[x] for idx, row in enumerate(forrest) if idx > y]

        if (
            check_visibility(tree_height, right)
            or check_visibility(tree_height, left)
            or check_visibility(tree_height, top)
            or check_visibility(tree_height, bottom)
        ):
            visible_trees += 1

print(visible_trees + visible_trees_edge)


# Part Two
views = []
for y in range(1, len(forrest) - 1):
    for x in range(1, len(forrest[0]) - 1):
        tree_height = forrest[y][x]

        right = forrest[y][x + 1:]
        left = forrest[y][:x]
        left.reverse()
        top = [row[x] for idx, row in enumerate(forrest) if idx < y]
        top.reverse()
        bottom = [row[x] for idx, row in enumerate(forrest) if idx > y]

        right_distance = check_distance(tree_height, right)
        left_distance = check_distance(tree_height, left)
        top_distance = check_distance(tree_height, top)
        bottom_distance = check_distance(tree_height, bottom)
        view_score = right_distance * left_distance * top_distance * bottom_distance

        views.append(view_score)

views.sort()
print(views[-1])
