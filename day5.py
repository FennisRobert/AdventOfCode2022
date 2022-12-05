import re
from string import ascii_uppercase

import aoc as aoc

lines = aoc.read_datafile("day5.txt")


class Stack:
    def __init__(self, letter: str):
        self.letter = letter

    def __repr__(self):
        return self.letter


stacks = [[] for i in range(9)]

for line in lines[:8]:
    for i, item in enumerate(line[1::4]):
        if item in ascii_uppercase:
            stacks[i].append(Stack(item))

[s.reverse() for s in stacks]
print(stacks)
for line in lines[10:]:
    N, frm, to = [int(x) for x in re.findall(r"\d+", line)]
    for n in range(N):
        stacks[to - 1].append(stacks[frm - 1].pop(-1))

print("".join([x[-1].letter for x in stacks]))


stacks = [[] for i in range(9)]

for line in lines[:8]:
    for i, item in enumerate(line[1::4]):
        if item in ascii_uppercase:
            stacks[i].append(Stack(item))

[s.reverse() for s in stacks]

for line in lines[10:]:
    N, frm, to = [int(x) for x in re.findall(r"\d+", line)]
    print(stacks)
    print(line)
    lift = stacks[frm - 1][-N:]
    stacks[frm - 1] = stacks[frm - 1][:-N]
    stacks[to - 1] = stacks[to - 1] + lift
    print(stacks)

print("".join([x[-1].letter for x in stacks]))
