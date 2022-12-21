from collections import defaultdict

import aoc as aoc

lines = aoc.read_datafile("day7.txt")


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Dir:
    def __init__(self, name):
        self.name = name
        self.dirs = []
        self.files = []

    def print(self, depth=0):
        sep = "  " * depth
        for dir in self.dirs:
            print(sep + f"{dir.name} - {dir.size}")
            dir.print(depth + 1)
        for file in self.files:
            print(sep + f"{file.name}: {file.size}")

    @property
    def size(self):
        size = 0
        if self.files:
            size += sum([f.size for f in self.files])
        if self.dirs:
            size += sum([d.size for d in self.dirs])
        return size

    @property
    def dirdict(self):
        return {dir.name: dir for dir in self.dirs}

    @property
    def subdirs(self):
        return [dir.name for dir in self.dirs]

    def dir(self, dirtree: list):
        current_dir = self
        for dir in dirtree[1:]:
            current_dir = current_dir(dir)
        return current_dir

    def _add_dir(self, name):
        self.dirs.append(Dir(name))

    def add_file(self, name, size):
        self.files.append(File(name, size))

    def __call__(self, dirname):
        if not dirname in self.dirdict:
            self._add_dir(dirname)
        return self.dirdict[dirname]


dirtree = []

mdir = Dir("/")

for line in lines:
    items = line.split()
    if items[0] == "$":
        if items[1] == "cd":
            if items[2] == "..":
                dirtree = dirtree[:-1]
                continue
            dirtree.append(items[2])
            continue
        if items[1] == "ls":
            continue
    elif items[0] == "dir":
        continue
    size = int(items[0])
    name = items[1]
    mdir.dir(dirtree).add_file(name, size)

mdir.print()


def collect(dir: Dir, dirlist: list):
    for subdir in dir.dirs:
        if subdir.size <= 100_000:
            dirlist.append((subdir.name, subdir.size))
            collect(subdir, dirlist)
        else:
            collect(subdir, dirlist)
    return dirlist


dirlist = collect(mdir, [])

print("answer part 1:", sum([x[1] for x in dirlist]))


def collect(dir: Dir, dirlist: list):
    for subdir in dir.dirs:
        dirlist.append((subdir.name, subdir.size))
        dirlist = collect(subdir, dirlist)
    return dirlist


diff = 30_000_000 - (70_000_000 - mdir.size)
print(f"Required size: {diff}")

dirlist = sorted(collect(mdir, []), key=lambda x: x[1])
for name, value in dirlist:
    if value >= diff:
        print("First valid option:", name, value)
        break
