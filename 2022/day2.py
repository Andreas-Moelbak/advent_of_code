

with open("./day2.input", "r") as f:
    data = f.read().split("\n")

points = 0
# X, Y, Z = 1, 2, 3
# A, B, C = 1, 2, 3

# X, Y, Z = 0, 3, 6

# Sten = 1
# papp = 2
# Saks = 3

score_bord = {'ax': 4, 'ay': 8, 'az': 3, 'bx': 1, 'by': 5, 'bz': 9, 'cx': 7, 'cy': 2, 'cz': 6}
for spil in data:
    spil = spil.lower().replace(" ", "")
    if spil:
        points += score_bord[spil]

print(points)


score_bord = {'ax': 3, 'ay': 4, 'az': 8, 'bx': 1, 'by': 5, 'bz': 9, 'cx': 2, 'cy': 6, 'cz': 7}

points = 0
for spil in data:
    spil = spil.lower().replace(" ", "")
    if spil:
        points += score_bord[spil]

print(points)
