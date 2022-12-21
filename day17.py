import itertools
from collections import defaultdict

import numpy as np

import aoc as aoc

groups = aoc.group_read("day17test.txt")

instructions = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
instructions = aoc.read_datafile("day17.txt")[0]
rocks = []
for i, group in enumerate(groups):
    subrock = []
    for r, line in enumerate(group):
        for c, ch in enumerate(line):
            if ch != "#":
                continue
            subrock.append((c, len(group) - r - 1))
    rocks.append(subrock)


def iterrocks():
    while True:
        for n, r in enumerate(rocks):
            yield n + 1, r


def iterinstr(toloop):
    while True:
        for ii, c in enumerate(toloop):
            yield ii + 1, c


def moverock(rock, pos):
    return [(x + pos[0], y + pos[1]) for x, y in rock]


def printworld(world, addrock=None):
    symb = {0: ".", 1: "#"}
    world2 = defaultdict(int)
    world2.update(world)
    if addrock is not None:
        for xx, yy in addrock:
            world2[xx, yy] = 1
    highest = max([y for x, y in world2.keys() if world2[(x, y)] == 1])

    for yy in range(highest + 1, 0, -1):
        print("|" + "".join([symb[world2[(xx, yy)]] for xx in range(1, 8)]) + "|")
    print("+-------+")
    print("")


def can_move_to(rock: list, pos: tuple, world: defaultdict):
    rock2 = [(x + pos[0], y + pos[1]) for x, y in rock]
    for x, y in rock2:
        if x < 1:
            return False
        if x > 7:
            return False
        if y < 1:
            return False
        if world[(x, y)] == 1:
            return False
    return True


# iters = 2022
maxh = lambda w: max([0] + [y for x, y in w.keys() if w[(x, y)] == 1])


def calc_height(iters):
    world = defaultdict(int)
    iterloop = iterinstr(instructions)
    highest = 0
    ii = 0
    for NR, Rock in iterrocks():
        ii += 1
        x0, y0 = 3, highest + 4
        # printworld(world, moverock(Rock, (x0, y0)))
        while True:
            iinstr, i = next(iterloop)
            if iinstr == 1:
                print(NR, ii, maxh(world))
            if (iinstr == 1) and (NR == 1):
                print("Repetition after:", ii)
            if i == ">":
                x1 = x0 + 1
            else:
                x1 = x0 - 1
            if can_move_to(Rock, (x1, y0), world):
                x0 = x1
            y1 = y0 - 1

            if can_move_to(Rock, (x0, y1), world):
                y0 = y1
                # printworld(world, moverock(Rock, (x0, y0)))
            else:
                for rx, ry in Rock:
                    world[(rx + x0, ry + y0)] = 1
                    highest = max(highest, ry + y0)
                # highest = max([y for x, y in world.keys()])
                break

        if ii >= iters:
            break
    return maxh(world)


totnum = 1_000_000_000_000

calc_height(10000)
print("Ninstructions", len(instructions), len(instructions) * 5)
xs = np.array([1719, 3444, 5169, 6894, 8619])
ys = np.array([2689, 5417, 8145, 10873, 13601])

xs = np.array([9, 44, 79, 114])
ys = np.array([15, 70, 123, 176])
print(xs[1:] - xs[:-1], ys[1:] - ys[:-1])

loopsize = 1725
heightloop = 2728

# loopsize = 35
# heightloop = 53

# l0 = 9
# h0 = 15
l0 = 1719

l1 = l0
l2 = l0 + loopsize
l3 = l0 + 2 * loopsize

h1 = calc_height(l0)
h2 = calc_height(l0 + loopsize)
h3 = calc_height(l0 + loopsize * 2)

Nloops = np.floor((totnum - l2) / loopsize)
Nleft = totnum - l2 - Nloops * loopsize

h4 = calc_height(l0 + loopsize * 2 + Nleft)

print(h1, h2, h3, h4)
print(h2 - h1, h3 - h2, h4 - h3)
print(h3 + (Nloops - 1) * (h3 - h2) + (h4 - h3))


Nloops = int(np.floor(totnum / (len(instructions) * 5)))
print("Nloops", Nloops)

height_one_loop = 308

HeightNLoops = Nloops * height_one_loop

iters = totnum - Nloops * len(instructions) * 5
iters = len(instructions) * 5 * 2
