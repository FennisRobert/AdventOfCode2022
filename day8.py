import numpy as np

import aoc as aoc

lines = aoc.read_datafile("day8.txt")

nx = len(lines[0])
ny = len(lines)

H = np.zeros((nx, ny), dtype=np.int32)
V = np.ones(H.shape)
V[1:-1, 1:-1] = 0
for i, line in enumerate(lines):
    H[i, :] = [int(x) for x in line]


for x in range(4):
    for i, row in enumerate(H):
        for j, t in enumerate(row):
            if j == 0:
                continue
            if t > np.max(row[0:j]):
                V[i, j] = 1
                highest = t
    V = np.rot90(V)
    H = np.rot90(H)

print(V)
print(np.sum(np.sum(V)))


S = np.ones(H.shape)
for x in range(4):
    for i, row in enumerate(H):
        for j, t in enumerate(row):
            for n, t2 in enumerate(row[j + 1 :]):
                if t2 >= t or n == (len(row[j + 1 :]) - 1):
                    S[i, j] = S[i, j] * (n + 1)
                    break

    S = np.rot90(S)
    H = np.rot90(H)
print(S)
print(np.max(np.max(S)))
