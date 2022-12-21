from collections import defaultdict

import aoc as aoc

lines = aoc.read_datafile("day18.txt")

cubes = [eval("(" + x + ")") for x in lines]

# c0 = cubes.pop(0)
setcubes = set(cubes)

volume = 0
surface = 0


def neighbors(cube):
    x, y, z = cube
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]


xs, ys, zs = list(zip(*cubes))

for cube in cubes:
    a0 = 6
    nextcubes = []
    for subcube in neighbors(cube):
        if subcube not in cubes:
            continue
        a0 -= 1
        nextcubes.append(subcube)
    surface += a0
    volume += 1


print("Part 1:", surface)

xmin, xmax = (min(xs) - 1, max(xs) + 1)
ymin, ymax = (min(ys) - 1, max(ys) + 1)
zmin, zmax = (min(zs) - 1, max(zs) + 1)


def inside(xyz):
    x, y, z = xyz
    return (xmin <= x <= xmax) and (ymin <= y <= ymax) and (zmin <= z <= zmax)


s0 = (xmin, ymin, zmin)

box = set()
newbound = [s0]
toadd = []
while True:
    toadd = []
    for b in newbound:
        for nb in neighbors(b):
            if inside(nb) and (nb not in box) and (nb not in cubes):
                toadd.append(nb)
                box.add(nb)
    newbound = toadd
    if len(toadd) == 0:
        break

sbox = 0
for cube in box:
    a0 = 6
    nextcubes = []
    for subcube in neighbors(cube):
        if subcube not in box:
            continue
        a0 -= 1
        nextcubes.append(subcube)
    sbox += a0

W = xmax - xmin + 1
D = ymax - ymin + 1
H = zmax - zmin + 1

print("Part 2:", sbox - 2 * (W * D + W * H + D * H))
