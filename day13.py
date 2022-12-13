from functools import cmp_to_key

import aoc as aoc

groups = aoc.group_read("day13.txt")
sum = 0

isint = lambda x: isinstance(x, int)
islist = lambda x: isinstance(x, list)


def ordered(l1: list, l2: list):
    # print(l1, l2)
    for a, b in zip(l1, l2):
        if isint(a) and isint(b):
            if a < b:
                return -1
            if b < a:
                return 1
            if a == b:
                continue
        if islist(a) and islist(b):
            ans = ordered(a, b)
            if ans in (-1, 1):
                return ans
        if islist(a) and isint(b):
            ans = ordered(a, [b])
            if ans in (-1, 1):
                return ans
        if isint(a) and islist(b):
            ans = ordered([a], b)
            if ans in (-1, 1):
                return ans
    # print(len(l1), len(l2))
    if len(l1) < len(l2):
        return -1
    elif len(l1) > len(l2):
        return 1
    else:
        return 0


sumval = 0
groups2 = []
for i, group in enumerate(groups):
    set1, set2 = [eval(x) for x in group]
    groups2.append(set1)
    groups2.append(set2)
    ans = ordered(set1, set2)
    if ans == -1:
        sumval = sumval + i + 1

    if ans == 0:
        print(i, "Error!", ans)

print(sumval)

# 8131 too high
# groups2 = [[eval(x1), eval(x2)] for (x1, x2) in groups]
groups2.append([[2]])
groups2.append([[6]])
groups2 = sorted(groups2, key=cmp_to_key(ordered))

i1 = groups2.index([[2]])
i2 = groups2.index([[6]])
print((i1 + 1) * (i2 + 1))
