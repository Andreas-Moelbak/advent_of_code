with open("./day4.input", "r") as f:
    data = f.read().strip().split("\n")


sum1 = 0
sum2 = 0

for i in data:
    elf1, elf2 = i.split(",")
    elf1_begin, elf1_end = map(int, elf1.split("-"))
    elf2_begin, elf2_end = map(int, elf2.split("-"))

    if (
        (elf1_begin >= elf2_begin and elf1_end <= elf2_end)
        or (elf2_begin >= elf1_begin and elf2_end <= elf1_end)
    ):
        sum1 += 1

    if (
        (elf1_begin >= elf2_begin and elf1_begin <= elf2_end)
        or (elf1_begin <= elf2_begin and elf1_end >= elf2_end)
        or (elf2_begin >= elf1_begin and elf2_begin <= elf1_end)
        or (elf2_begin <= elf1_begin and elf2_end >= elf1_end)
    ):
        sum2 += 1


print(sum1)
print(sum2)
