from string import ascii_lowercase

import aoc as aoc

lines = aoc.read_datafile("day3.txt")

sumvalue = 0

valuedict = dict()
for i, char in enumerate(ascii_lowercase):
    valuedict[char] = i + 1
    valuedict[char.upper()] = i + 27

for line in lines:
    N = len(line)
    c1 = line[0 : N // 2]
    c2 = line[N // 2 :]

    common = set(c1).intersection(set(c2))
    sumvalue = sumvalue + sum([valuedict[c] for c in common])

print(sumvalue)

sumvalue = 0


for (e1, e2, e3) in aoc.iter_groups(lines, 3):
    common = set(e1).intersection(set(e2)).intersection(set(e3))
    sumvalue = sumvalue + valuedict[list(common)[0]]

print(sumvalue)
