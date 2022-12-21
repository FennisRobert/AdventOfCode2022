import aoc as aoc

lines = aoc.read_datafile("day4.txt")

N = 0
N2 = 0
for line in lines:
    sec1, sec2 = line.split(",")
    s1s, s1e = [int(x) for x in sec1.split("-")]
    s2s, s2e = [int(x) for x in sec2.split("-")]
    set1 = set(range(s1s, s1e + 1))
    set2 = set(range(s2s, s2e + 1))
    if set1.issubset(set2) or set2.issubset(set1):
        N = N + 1
    if not set1.isdisjoint(set2):
        N2 += 1
print(N)
print(N2)
