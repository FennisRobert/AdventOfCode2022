import aoc as aoc

lines = aoc.read_datafile("day10.txt")


class System:
    def __init__(self):
        self.c = 0
        self.signal_strength = 0
        self.reg = 1
        self.img = ""

    def next(self):
        self.c += 1
        if self.c == 20 or (self.c - 20) % 40 == 0:
            self.signal_strength += self.reg * self.c
        if abs(self.reg - ((self.c - 1) % 40)) < 2:
            self.img += "#"
        else:
            self.img += " "


sys = System()

for line in lines:
    sys.next()
    if line == "noop":
        continue
    else:
        add = int(line.split(" ")[1])
        sys.next()
        sys.reg += add

print(f"Part 1: {sys.signal_strength}")
print("Part 2")
for i in range(6):
    print("|" + sys.img[i * 40 : (i + 1) * 40] + "|")
