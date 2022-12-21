import aoc as aoc

lines = aoc.read_datafile("day3data.txt")

keep = list(range(len(lines)))

for i in range(12):
    one_set = []
    zero_set = []
    sets = [zero_set, one_set]

    for j in keep:
        sets[int(lines[j][i])].append(j)

    if len(one_set) > len(zero_set):
        keep = one_set
    elif len(one_set) < len(zero_set):
        keep = zero_set
    elif len(one_set) == len(zero_set):
        keep = one_set
    if len(keep) == 1:
        break

oxnum = int(lines[keep[0]], 2)

keep = list(range(len(lines)))

for i in range(12):
    one_set = []
    zero_set = []
    sets = [zero_set, one_set]

    for j in keep:
        sets[int(lines[j][i])].append(j)
    if len(one_set) > len(zero_set):
        keep = zero_set
    elif len(one_set) < len(zero_set):
        keep = one_set
    elif len(one_set) == len(zero_set):
        keep = zero_set
    print(i, [lines[k][: i + 1] + "-" + lines[k][i + 1 :] for k in keep])
    if len(keep) == 1:
        break

othernum = int(lines[keep[0]], 2)

print(oxnum * othernum)
