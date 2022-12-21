import re

import numpy as np

import aoc as aoc

trans = {-1: "#", -2: ".", 0: " ", 10: "o"}


def printw(W: np.ndarray):
    for row in W:
        print("".join([trans[x] for x in row]))


lines = aoc.read_datafile("day14test.txt")
lineinstr = []
xs = []
ys = []
for line in lines:
    lineinstr.append(
        [(int(x[1]), int(x[2])) for x in re.findall(r"((\d+)\,(\d+))", line)]
    )
    xs = xs + [x[0] for x in lineinstr[-1]]
    ys = ys + [x[1] for x in lineinstr[-1]]
xs.append(500)
ys.append(0)

minx = min(xs) - 5
maxx = max(xs) + 5
miny = min(ys) - 2
maxy = max(ys) + 3

start = (500 - minx, 0 - miny)

W = np.zeros((maxy - miny, maxx - minx))

for instr in lineinstr:
    for p1, p2 in zip(instr[0:-1], instr[1:]):
        x1, x2 = p1[0] - minx, p2[0] - minx
        y1, y2 = p1[1] - miny, p2[1] - miny
        W[min(y1, y2) : max(y1, y2) + 1, min(x1, x2) : max(x1, x2) + 1] = -1

Spawning = True
while Spawning:
    gxy = list(start)
    while True:
        if gxy[1] + 1 == maxy - miny:
            Spawning = False
            break
        elif W[gxy[1] + 1, gxy[0]] == 0:
            gxy[1] += 1
            continue
        elif W[gxy[1] + 1, gxy[0] - 1] == 0:
            gxy[0] -= 1
            gxy[1] += 1
            continue
        elif W[gxy[1] + 1, gxy[0] + 1] == 0:
            gxy[0] += 1
            gxy[1] += 1
            continue
        else:
            W[gxy[1], gxy[0]] = -2
            break

printw(W)
print(np.count_nonzero(W == -2))


## part2
minx = min(xs) - 15
maxx = max(xs) + 15
miny = min(ys) - 2
maxy = max(ys) + 3
start = (500 - minx, 0 - miny)
W = np.zeros((maxy - miny, maxx - minx))
for instr in lineinstr:
    for p1, p2 in zip(instr[0:-1], instr[1:]):
        x1, x2 = p1[0] - minx, p2[0] - minx
        y1, y2 = p1[1] - miny, p2[1] - miny
        W[min(y1, y2) : max(y1, y2) + 1, min(x1, x2) : max(x1, x2) + 1] = -1


W[-1, :] = -1
W[start[1], start[0]] = 10
Spawning = True
while Spawning:
    gxy = list(start)
    while True:
        if W[gxy[1] + 1, gxy[0]] == 0:
            gxy[1] += 1
            continue
        elif W[gxy[1] + 1, gxy[0] - 1] == 0:
            gxy[0] -= 1
            gxy[1] += 1
            continue
        elif W[gxy[1] + 1, gxy[0] + 1] == 0:
            gxy[0] += 1
            gxy[1] += 1
            continue
        elif gxy == list(start):
            Spawning = False
            break
        else:
            W[gxy[1], gxy[0]] = -2
            break
printw(W)
print(np.count_nonzero(W == -2) + 1)
