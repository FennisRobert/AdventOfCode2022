import numpy as np

import aoc as aoc


class Symbol:
    def __init__(self, num: int):
        self.num = num


class SymbolList:
    def __init__(self, itemlist: list):

        self.items: list[Symbol] = [Symbol(x) for x in itemlist]

    def num(self, number):
        for symb in self.items:
            if symb.num == number:
                return symb
        return None

    def process(self):
        N = len(self.items)
        lst = [x for x in self.items]
        for symbol in self.items:
            i1 = lst.index(symbol)
            i2 = int(np.floor((i1 + 0.5 * np.sign(symbol.num) + symbol.num) % (N - 1)))
            item = lst.pop(i1)
            lst.insert(i2, item)
            print(symbol.num, [x.num for x in lst])

        print([x.num for x in lst])
        i0 = lst.index(self.num(0))
        i1 = (i0 + 1000) % N
        i2 = (i0 + 2000) % N
        i3 = (i0 + 3000) % N
        print(i1, i2, i3)
        return i1 + i2 + i3


lines = aoc.read_datafile("day20test.txt")

nums = [int(x) for x in lines]

SL = SymbolList(nums)

print("Part1: ", SL.process())
