import numpy as np

import aoc as aoc

groups = aoc.group_read("day4_2021.txt")

nums = [
    14,
    30,
    18,
    8,
    3,
    10,
    77,
    4,
    48,
    67,
    28,
    38,
    63,
    43,
    62,
    12,
    68,
    88,
    54,
    32,
    17,
    21,
    83,
    64,
    97,
    53,
    24,
    2,
    60,
    96,
    86,
    23,
    20,
    93,
    65,
    34,
    45,
    46,
    42,
    49,
    71,
    9,
    61,
    16,
    31,
    1,
    29,
    40,
    59,
    87,
    95,
    41,
    39,
    27,
    6,
    25,
    19,
    58,
    80,
    81,
    50,
    79,
    73,
    15,
    70,
    37,
    92,
    94,
    7,
    55,
    85,
    98,
    5,
    84,
    99,
    26,
    66,
    57,
    82,
    75,
    22,
    89,
    74,
    36,
    11,
    76,
    56,
    33,
    13,
    72,
    35,
    78,
    47,
    91,
    51,
    44,
    69,
    0,
    90,
    52,
]
print(groups)

numcounter = []

for i, group in enumerate(groups):
    board = [[int(x) for x in line.split()] for line in group]
    numboard = np.array(board)
    stripeoff = np.zeros(numboard.shape)

    for k, n in enumerate(nums):
        stripeoff[numboard == n] = 1
        if any(np.sum(stripeoff, 0) == 5) or any(np.sum(stripeoff, 1) == 5):
            numcounter.append((k, np.sum(numboard[stripeoff == 0][:]) * n))
            break

print(sorted(numcounter, key=lambda x: x[0]))
