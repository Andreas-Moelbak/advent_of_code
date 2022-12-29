letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = dict(zip(letters, [letters.index(i)+1 for i in letters]))
# priority = dict(zip(letters, range(1, len(letters)+1)))


with open("./day3.input", "r") as f:
    data = f.read().strip().split("\n")

sum = 0
for i in data:
    compartment1 = i[:int(len(i)/2)]
    compartment2 = i[int(len(i)/2):]
    for j in compartment1:
        if j in compartment2:
            print(j)
            sum += priority[j]
            break

print(sum)

sum = 0
list_of_groups = list(zip(*(iter(data),)*3))
for i in list_of_groups:
    for j in i[0]:
        if j in i[1] and j in i[2]:
            sum += priority[j]
            break

print(sum)
