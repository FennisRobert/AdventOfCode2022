import re
from functools import reduce

import numpy as np

import aoc as aoc

lines = aoc.group_read("day11.txt")


class Monkey:
    def __init__(self, thinglist: list):
        self.nr = int(thinglist[0].split(" ")[1].replace(":", ""))
        self.items = [int(x.strip()) for x in thinglist[1].split(":")[1].split(",")]
        self.func = eval(
            "lambda old: ("
            + thinglist[2].split(":")[1].replace(" ", "").split("=")[1]
            + ")"
        )
        self.div = int(re.findall("\d+", thinglist[3])[0])
        self.iftrue = int(re.findall("\d+", thinglist[4])[0])
        self.iffalse = int(re.findall("\d+", thinglist[5])[0])
        self.ninspect = 0

    def doturn(self, monkeylist: dict):
        for item in self.items:
            self.ninspect += 1
            new = self.func(item)
            # new = (new // 3) + (new % 3)
            if new % self.div == 0:
                monkeylist[self.iftrue].receive(new)
            else:
                monkeylist[self.iffalse].receive(new)
        self.items = []

    def receive(self, item: int):
        val = 3 * 13 * 2 * 11 * 19 * 17 * 5 * 7
        n = val + (item % val)
        self.items.append(n)


monkeys = dict()

for group in lines:
    m = Monkey(group)
    monkeys[m.nr] = m

nrlist = sorted([m.nr for m in monkeys.values()])
Nturns = 10_000

for i in range(Nturns):
    print(i)
    for monkeynr in nrlist:
        if not monkeys[monkeynr].items:
            continue
        monkeys[monkeynr].doturn(monkeys)

activity = sorted([m.ninspect for m in monkeys.values()])
print(activity)
print(activity[-1] * activity[-2])
