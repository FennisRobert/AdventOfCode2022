import numpy as np

import aoc as aoc

lines = aoc.read_datafile("day2.txt")


score = 0
valueo = {"A": 1, "B": 2, "C": 3}
value = {"X": 1, "Y": 2, "Z": 3}

for line in lines:
    p1, p2 = line.split(" ")
    score = score + value[p2]
    if valueo[p1] == value[p2]:
        score = score + 3
        continue
    if p1 == "A":
        if p2 == "Y":
            score = score + 6
            continue
        if p2 == "Z":
            continue
    if p1 == "B":
        if p2 == "Z":
            score = score + 6
            continue
        if p2 == "X":
            continue
    if p1 == "C":
        if p2 == "X":
            score = score + 6
            continue
print(score)


valueo = {"A": 0, "B": 1, "C": 2}
value = {"X": 0, "Y": 3, "Z": 6}
score = 0
for line in lines:
    p1, p2 = line.split(" ")
    score = score + value[p2]

    p11 = np.exp(1j * valueo[p1] * 2 * np.pi / 3)
    rot = np.exp(1j * 2 * np.pi / 3)

    if p2 == "X":
        p22 = p11 / rot
    if p2 == "Z":
        p22 = p11 * rot
    if p2 == "Y":
        p22 = p11
    ang = np.angle(p22) * 3 / (2 * np.pi)
    if ang < 0:
        ang = 3 + ang
    nump2 = ang + 1
    score = score + nump2

print(score)
