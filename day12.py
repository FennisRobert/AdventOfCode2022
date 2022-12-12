from string import ascii_lowercase

import numpy as np

import aoc as aoc

values = {a: i for (i, a) in enumerate(ascii_lowercase)}
values["S"] = values["a"]
values["E"] = values["z"]
lines = aoc.read_datafile("day12.txt")

X = len(lines[0])
Y = len(lines)
H = np.zeros((Y, X))
end = None
start = None

startpoints = []
for r, line in enumerate(lines):
    H[r, :] = [values[c] for c in line]
    for j, c in enumerate(line):
        if c == "E":
            end = (r, j)
        if c == "S":
            start = (r, j)
        if c == "S" or c == "a":
            startpoints.append((r, j))


def options(pin: tuple) -> list:
    i, j = pin
    p1 = (i + 1, j)
    p2 = (i - 1, j)
    p3 = (i, j + 1)
    p4 = (i, j - 1)
    opts = [p1, p2, p3, p4]
    return [p for p in opts if 0 <= p[0] < Y and 0 <= p[1] < X]


endnp = np.array(end)
path = (start,)
visited = {start: (start,)}  # part 1
visited = {s: (s,) for s in startpoints}  # part 2

while len(visited) < Y * X:
    print(len(visited) / (X * Y) * 100)
    newvisited = dict()
    for v in visited.keys():
        opts2 = options(v)
        for opt in opts2:
            if H[opt] > H[v] + 1:
                continue
            if opt in visited:
                path = visited[v] + (opt,)
                if len(path) < len(visited[opt]):
                    visited[opt] = path
                continue
            newvisited[opt] = visited[v] + (opt,)
    if len(newvisited) == 0:
        break
    visited.update(newvisited)

print("solution:", len(visited[end]) - 1)

print(visited[end])
