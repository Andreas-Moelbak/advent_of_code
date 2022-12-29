#!/usr/bin/env python3

with open("day5.input", "r") as file:
    stacks, instructions = file.read().split("\n\n")


print(stacks)
print()
stacks = stacks.split("\n")
stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []
for i, v in enumerate(stacks, 1):
    stack1.append(v[1:2])
    stack2.append(v[5:6])
    stack3.append(v[9:10])
    stack4.append(v[13:14])
    stack5.append(v[17:18])
    stack6.append(v[21:22])
    stack7.append(v[25:26])
    stack8.append(v[29:30])
    stack9.append(v[33:34])

    if i == len(stacks)-1:
        break

stacks = []
stacks.append(stack1)
stacks.append(stack2)
stacks.append(stack3)
stacks.append(stack4)
stacks.append(stack5)
stacks.append(stack6)
stacks.append(stack7)
stacks.append(stack8)
stacks.append(stack9)

newStack = [list(filter((' ').__ne__, stack)) for stack in stacks]

ins = []
for i in instructions.strip().split("\n"):
    ins.append(list(map(int, i.split()[1::2])))

for idx, i in enumerate(ins):
    antal, fra, til = i[0], i[1]-1, i[2]-1

    tmpStack = newStack[fra][:antal]
    newStack[fra] = newStack[fra][antal:]
    # Uncomment to solve part 2
    # tmpStack.reverse()
    for crate in tmpStack:
        newStack[til].insert(0, crate)

for i in newStack:
    print(i[0], end='')
