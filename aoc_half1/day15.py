import re

import numpy as np

import aoc as aoc

pattern = re.compile(
    r"Sensor at x=([-+\d]+), y=([-+\d]+): closest beacon is at x=([-+\d]+), y=([-+\d]+)"
)
lines = aoc.read_datafile("day15.txt")

y0 = 10

print(4_000_000 * 3337614 + 2933732)


def mdist(x, y, x0, y0):
    return np.abs(x - x0) + np.abs(y - y0)


sxs = []
sys = []
bxs = []
bys = []

xnot = set()
for line in lines:
    sx, sy, bx, by = [int(x) for x in re.findall(pattern, line)[0]]
    sxs.append(sx)
    sys.append(sy)
    bxs.append(bx)
    bys.append(by)

    dist = mdist(sx, sy, bx, by)
    xd = max(0, dist - np.abs(sy - y0))
    th = set(range(sx - xd, sx + xd))
    # print(th)
    xnot = xnot.union(th)
    # xnot.remove(bx)

print(len(xnot))
xpos = np.array([])
ypos = np.array([])

vmax = 4000000
for sx, sy, bx, by in zip(sxs, sys, bxs, bys):
    # sx, sy, bx, by = [int(x) for x in re.findall(pattern, line)[0]]
    dist = mdist(sx, sy, bx, by) + 1
    xrange = np.arange(max(0, sx - dist), min(vmax, sx + dist + 1))

    yrange1 = sy + (dist - np.abs(xrange - sx))
    yrange2 = sy - (dist - np.abs(xrange[1:-1] - sx))

    xrange = np.concatenate((xrange, xrange[1:-1]))
    yrange = np.concatenate((yrange1, yrange2))

    xrange = xrange[(0 <= yrange) & (yrange <= vmax)]
    yrange = yrange[(0 <= yrange) & (yrange <= vmax)]

    xpos = np.concatenate((xpos, xrange))
    ypos = np.concatenate((ypos, yrange))

xnot = set()
possible = np.ones(xpos.shape)


for sx, sy, bx, by in zip(sxs, sys, bxs, bys):
    dist = mdist(sx, sy, bx, by)
    d = mdist(xpos, ypos, sx, sy)
    possible[d <= dist] = 0
    possible[(xpos == bx) & (ypos == by)] = 0
    possible[(xpos == sx) & (ypos == sy)] = 0

print(xpos[possible == 1], ypos[possible == 1])
