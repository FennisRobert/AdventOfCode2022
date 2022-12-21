import re

import aoc as aoc


class Valve:
    def __init__(self, name: str, flowrate: int, con: list, tree: dict):
        self.name = name
        self.flowrate = flowrate
        self.con = con
        self.tree = tree

    def build_tree(self, tree: dict = None) -> dict:
        if tree is None:
            tree = {self.name: []}
        for v in self.con:
            path = tree[self.name] + [self.name]
            if v in tree:
                if len(path) < len(tree[v]):
                    tree[v] = path
                    tree = self.tree[v].build_tree(tree)
            else:
                tree[v] = path
                tree = self.tree[v].build_tree(tree)
        return tree

    def get_options(self, minutes: int, subset: dict):
        tree = self.build_tree()
        options = []
        for valve in subset:
            options.append(
                (
                    valve,
                    (minutes - len(tree[valve]) - 1) * self.tree[valve].flowrate,
                    len(tree[valve]) + 1,
                )
            )
        return options


lines = aoc.read_datafile("day16.txt")

pat = re.compile(
    r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z\,\s]+)"
)

valves = dict()

for line in lines:
    valve, flowstr, connectstr = re.findall(pat, line)[0]
    flow = int(flowstr)
    connect = connectstr.split(", ")
    valves[valve] = Valve(valve, flow, connect, valves)

value_valves = [v for v in valves.keys() if valves[v].flowrate > 0]
print(value_valves)
minutes = 30
valve = "AA"
nbest = len(value_valves)

routes = [(["AA"], 30, 0)]

for i in range(len(value_valves)):
    routes2 = []
    for route in routes:
        lv = route[0][-1]
        opts = valves[lv].get_options(route[1], value_valves)
        opts = sorted(opts, key=lambda x: x[1], reverse=True)
        opts = [o for o in opts if o[0] not in route[0] and o[2] <= route[1]]
        # print(opts)
        if len(opts) == 0:
            routes2.append(route)
            continue
        for dest, val, time in opts[0:nbest]:
            routes2.append((route[0] + [dest], route[1] - time, route[2] + val))

    routes = routes2
    routes = sorted(routes, key=lambda x: x[2], reverse=True)[:1000]
    # if len(routes2) == len(routes):
    #    break
    # print(routes)
    # input("")

print(sorted(routes, key=lambda x: x[2], reverse=True)[0])


routes = [((["AA"], ["AA"]), (26, 26), 0)]
nclean = 2
for i in range(len(value_valves)):
    routes2 = []
    no_opts = True
    for route in routes:
        lv1 = route[0][0][-1]
        lv2 = route[0][1][-1]

        opts1 = valves[lv1].get_options(route[1][0], value_valves)
        opts2 = valves[lv2].get_options(route[1][1], value_valves)

        opts1 = sorted(opts1, key=lambda x: x[1], reverse=True)
        opts1 = [
            o
            for o in opts1
            if o[0] not in route[0][0] + route[0][1] and o[2] <= route[1][0]
        ]

        opts2 = sorted(opts2, key=lambda x: x[1], reverse=True)
        opts2 = [
            o
            for o in opts2
            if o[0] not in route[0][0] + route[0][1] and o[2] <= route[1][1]
        ]
        # print(opts)
        if len(opts1) == 0 and len(opts2) == 0:
            routes2.append(route)
            continue

        for dest1, val1, time1 in opts1[0:nbest]:
            no_opts = False
            for dest2, val2, time2 in opts2[0:nbest]:
                if dest2 == dest1:
                    continue
                routes2.append(
                    (
                        (route[0][0] + [dest1], route[0][1] + [dest2]),
                        (route[1][0] - time1, route[1][1] - time2),
                        route[2] + val1 + val2,
                    )
                )
    if no_opts is True:
        break
    routes = routes2
    if i >= nclean:
        routes = sorted(routes, key=lambda x: x[2], reverse=True)[:100_000]
    # if len(routes2) == len(routes):
    #    break
    print(routes)

print(sorted(routes, key=lambda x: x[2], reverse=True)[0])
