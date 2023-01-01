with open("./day1.input", "r") as f:
    elfs = f.read().split("\n\n")

convertedElfFood = []
for elf in elfs:
    totalFood = sum([int(food) for food in elf.split()])
    convertedElfFood.append(totalFood)

convertedElfFood.sort()
# part1
print(*convertedElfFood[-1:])
# part2
print(sum(convertedElfFood[-3:]))
