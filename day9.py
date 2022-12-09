import numpy as np

import aoc as aoc

lines = aoc.read_datafile("day9.txt")

N = 10

rope = [np.array([0, 0]) for _ in range(N)]


dirs = {
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
}
points = set()
for line in lines:
    dr, vl = line.split(" ")
    ds = dirs[dr]
    for i in range(int(vl)):
        rope[0] = rope[0] + ds
        for k, T in enumerate(rope[1:]):
            dt = rope[k] - T
            DT = np.sign(dt) * round(max(abs(dt)) / 2)
            rope[k + 1] = rope[k + 1] + DT
            # if np.max(np.abs(dt)) > 1:
            #    rope[k + 1] = rope[k + 1] + DT
        points.add(tuple([int(x) for x in rope[-1]]))
print(len(points))
# 2460 6209
