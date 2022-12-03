from typing import Callable


def read_datafile(filename: str) -> list[str]:
    with open("data/" + filename, "r") as file:
        lines = [x for x in file.read().split("\n")]
        return lines


def group_read(filename: str) -> list[list]:
    with open("data/" + filename, "r") as file:
        lines = [[x for x in grp.split("\n")] for grp in file.read().split("\n\n")]
        return lines


def iter_groups(listin: list, groupsize: int, fmap: Callable = lambda x: x):
    groups = [listin[i::groupsize] for i in range(groupsize)]
    for group in zip(*groups):
        yield [fmap(x) for x in group]
