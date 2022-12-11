from collections import deque
import math

part1 = True
part2 = False

dat = list(map(str.split, open("input.txt").readlines()))

class Monkey:
    def __init__(self, lines):
        self.id = int(lines[0][1][:-1])
        self.items = deque()
        for i in lines[1][2:]:
            if ',' in i:
                self.items.append(int(i[:-1]))
            else:
                self.items.append(int(i))
        self.operation = (lines[2][4], lines[2][5])
        self.test = int(lines[3][-1])
        self.iftrue = int(lines[4][-1])
        self.iffalse = int(lines[5][-1])
        self.inspections = 0

    def __str__(self):
        return str(self.id, ": ", self.items)

    def operate(self, inp):
        if self.operation[1] == 'old':
            return inp * inp
        elif self.operation[0] == '*':
            return inp * int(self.operation[1])
        elif self.operation[0] == '+':
            return inp + int(self.operation[1])

    def take_round(self, p2, lcm):
        returns = []
        while len(self.items) > 0:
            if not p2:
                worry_level = self.operate(self.items.popleft()) // 3
            else:
                worry_level = self.operate(self.items.popleft()) % lcm
            if worry_level % self.test == 0:
                returns.append((worry_level, self.iftrue))
            else:
                returns.append((worry_level, self.iffalse))
            self.inspections += 1
        return returns


def get_monkeys():
    ms = []
    for i in range(0, len(dat), 7):
        ms.append(Monkey(dat[i:i+6]))
    return ms


def run_part1():
    monkeys = get_monkeys()

    for i in range(len(monkeys) * 20):
        changes = monkeys[i%len(monkeys)].take_round(False, 1)
        for j in changes:
            monkeys[j[1]].items.append(j[0])

    counts = []
    for i in monkeys:
        counts.append(i.inspections)
    counts.sort()

    return counts[-1] * counts[-2]


def run_part2():
    monkeys = get_monkeys()
    lcm = 1 # here's the magic - find the LCM of the 'test' values and keep the number smaller
    for i in monkeys:
        lcm = math.lcm(lcm, i.test)

    for i in range(len(monkeys) * 10000):
        changes = monkeys[i%len(monkeys)].take_round(True, lcm)
        for j in changes:
            monkeys[j[1]].items.append(j[0])

    counts = []
    for i in monkeys:
        counts.append(i.inspections)
    counts.sort()

    return counts[-1] * counts[-2]


print("1:", run_part1())
print("2:", run_part2())



