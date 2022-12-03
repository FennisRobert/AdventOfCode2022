def read_datafile(filename: str) -> list[str]:
    with open("data/" + filename, "r") as file:
        lines = [x for x in file.read().split("\n")]
        return lines


def group_read(filename: str) -> list[list]:
    with open("data/" + filename, "r") as file:
        lines = [[x for x in grp.split("\n")] for grp in file.read().split("\n\n")]
        return lines


def iter_groups(listin: list, groupsize: int):
    groups = [listin[i::groupsize] for i in range(groupsize)]
    for group in zip(*groups):
        yield group
