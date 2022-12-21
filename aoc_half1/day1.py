import aoc as aoc

lines = aoc.read_datafile("day1.txt")
test = aoc.group_read("day1.txt")
print(test)
print("hallo mijn man?")
elf_calories = []
counter = 0
for line in lines:
    if line == "":
        elf_calories.append(counter)
        counter = 0
    else:
        counter += int(line)
elf_calories.append(counter)


print(sum(sorted(elf_calories, reverse=True)[:3]))
