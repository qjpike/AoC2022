# TODO: Part2 could be better - could probably use slices more efficiently

dat = list(map(str.split, open("input.txt").readlines()))

from collections import deque

def read_stack_input():
    dat = open("in2.txt").readlines()
    dat.reverse()
    lanes = dat[0].split()
    stacks = list()
    for i in lanes:
        nxt = deque()
        for j in dat[1:]:
            idx = dat[0].index(i)
            if idx < len(j):
                if j[idx] != ' ':
                    nxt.append(j[idx])
        stacks.append(nxt)
    return stacks


starts = read_stack_input()

for command in dat:
    for j in range(int(command[1])):
        starts[int(command[-1])-1].append(starts[int(command[3])-1].pop())

print("1:", end = ' ')
for i in starts:
    print(i[-1], end='')
print()

starts = read_stack_input()
for command in dat:
    add = []
    for j in range(int(command[1])):
        add.append(starts[int(command[3])-1].pop())
    add.reverse()
    for j in add:
        starts[int(command[-1])-1].append(j)

print("2:", end=' ')
for i in starts:
    print(i[-1], end='')