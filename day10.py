import numpy as np

import aoc as aoc

lines = aoc.read_datafile("day10.txt")


class System:
    def __init__(self):
        self.c = 0
        self.signal_strength = 0
        self.reg = 1
        self.img = ""


sys = System()


def nextcycle(sys: System):
    sys.c += 1
    if sys.c == 20 or (sys.c - 20) % 40 == 0:
        sys.signal_strength += sys.reg * sys.c
    if abs(sys.reg - ((sys.c - 1) % 40)) < 2:
        sys.img += "#"
    else:
        sys.img += " "


for line in lines:
    nextcycle(sys)
    if line == "noop":
        continue
    else:
        add = int(line.split(" ")[1])
        nextcycle(sys)
        sys.reg += add

print(f"Part 1: {sys.signal_strength}")
print("Part 2")
for i in range(6):
    print("|" + sys.img[i * 40 : (i + 1) * 40] + "|")
