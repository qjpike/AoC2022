
dat = []
with open("input.txt") as f:
    for i in f.readlines():
        dat.append(i.split(","))


count = 0
count2 = 0
for i in dat:
    elf1 = set(range(int(i[0].split("-")[0]), int(i[0].split("-")[1]) + 1))
    elf2 = set(range(int(i[1].split("-")[0]), int(i[1].split("-")[1]) + 1))

    if elf1 & elf2 == elf1 or elf1 & elf2 == elf2:
        count += 1
    if len(elf1 & elf2) > 0:
        count2 += 1
print("1:", count)
print("2:", count2)
