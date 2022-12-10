from collections import deque

dat = list(map(str.split, open("input.txt").readlines()))

x = 1
cycle = 0
pipeline = [0, '  ','']
cmds = deque(dat)
sig_strength = 0

field_row_counter = 0
field = []
for i in range(6):
    field.append([' ']*40)

while len(cmds) > 0 or pipeline[1] == 'addx':
    if ((cycle%40) - 20) == 0:
        sig_strength += (cycle) * x

    if pipeline[0] != 0:
        pipeline[0] -= 1
    elif pipeline[1] == 'addx':
        x += pipeline[2]
        pipeline = [0, '', '']

    if len(cmds) > 0 and pipeline[1] != 'addx':
        inst = cmds.popleft()
        if inst[0] == 'addx':
            pipeline = [1, inst[0], int(inst[1])]
        else:
            pipeline = [0, '', '']

    sprite_pos = range(x - 1, x + 2)
    if cycle % 40 in sprite_pos:
        field[field_row_counter-1][cycle % 40] = "█"
    if cycle % 40 == 0:
        field_row_counter += 1

    cycle += 1


print("1:", sig_strength)

print("\n2:")
for y in range(len(field)):
    for x in range(len(field[0])):
        print(field[y][x],end='')
    print("")