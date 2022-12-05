# TODO: some half decent input handling?
# TODO: Part2 could be better - could probably use slices more efficiently

dat = list(map(str.strip, open("input.txt").readlines()))

from collections import deque

starts = list()

starts.append(deque(['D', 'B', 'J', 'V']))
starts.append(deque(['P', 'V', 'B', 'W', 'R', 'D', 'F']))
starts.append(deque(['R', 'G', 'F', 'L', 'D', 'C', 'W', 'Q']))
starts.append(deque(['W', 'J', 'P', 'M', 'L', 'N', 'D', 'B']))
starts.append(deque(['H', 'N', 'B', 'P', 'C', 'S', 'Q']))
starts.append(deque(['R', 'D', 'B', 'S', 'N', 'G']))
starts.append(deque(['Z', 'B', 'P', 'M', 'Q', 'F', 'S', 'H']))
starts.append(deque(['W', 'L', 'F']))
starts.append(deque(['S', 'V', 'F', 'M', 'R']))

def move(start, end):
    end.append(start.popleft())


for i in dat:
    command = i.split()
    for j in range(int(command[1])):
        starts[int(command[-1])-1].append(starts[int(command[3])-1].pop())

for i in starts:
    print(i[-1], end='')
print()

starts = list()

starts.append(deque(['D', 'B', 'J', 'V']))
starts.append(deque(['P', 'V', 'B', 'W', 'R', 'D', 'F']))
starts.append(deque(['R', 'G', 'F', 'L', 'D', 'C', 'W', 'Q']))
starts.append(deque(['W', 'J', 'P', 'M', 'L', 'N', 'D', 'B']))
starts.append(deque(['H', 'N', 'B', 'P', 'C', 'S', 'Q']))
starts.append(deque(['R', 'D', 'B', 'S', 'N', 'G']))
starts.append(deque(['Z', 'B', 'P', 'M', 'Q', 'F', 'S', 'H']))
starts.append(deque(['W', 'L', 'F']))
starts.append(deque(['S', 'V', 'F', 'M', 'R']))

for i in dat:
    command = i.split()
    add = []
    for j in range(int(command[1])):
        add.append(starts[int(command[3])-1].pop())
    add.reverse()
    for j in add:
        starts[int(command[-1])-1].append(j)

for i in starts:
    print(i[-1], end='')