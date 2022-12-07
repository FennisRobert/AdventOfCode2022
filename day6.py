import aoc as aoc

lines = aoc.read_datafile("day6.txt")
line = lines[0]
for i in range(len(line) - 3):
    if len(set(line[i : i + 14])) == 14:
        print(i + 14)
        break
