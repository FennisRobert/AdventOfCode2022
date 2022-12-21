import pylab

import aoc as aoc

lines = aoc.read_datafile("day21test.txt")
import numpy as np

l0 = lines[0]

tdict = {}
for line in lines:
    tdict[line.split(":")[0]] = line.split(":")[1]


func = tdict["root"]
root = None


def expand(expr):
    func = "lambda x: " + expr
    while True:
        try:
            root = eval(func)
            print(root(0))
            print(func)
            return root
            break
        except NameError as e:
            func = func.replace(e.name, "(" + tdict[e.name].replace(" ", "") + ")")
            # print(func)


print("Part1:", expand(func)(0))

tdict["humn"] = "x"
numa, numb = func.split("+")
f1, f2 = tdict[numa.strip()], tdict[numb.strip()]

f1 = expand(f1)
f2 = expand(f2)(0)

xs = np.linspace(-1e15, 1e15, 1000)
ys = f1(xs)

x1 = -1e15
x2 = 1e15
y1 = f1(x1)
y2 = f1(x2)
dydx = (y2 - y1) / (x2 - x1)
b = y1 - (dydx * x1)
print("Part2:", round((f2 - b) / dydx))
