from collections import deque

dat = list(map(str.split, open("input.txt").readlines()))

# Build the walls and floors
field = dict()
for i in dat:
    corners = deque()
    for j in i:
        if j == '->':
            continue
        else:
            corners.append((int(j.split(',')[0]), int(j.split(',')[1])))
    start = corners.popleft()
    while corners:
        end = corners.popleft()
        if start[0] == end[0]:
            for k in range(min(start[1], end[1]), max(start[1], end[1])+1):
                field[(start[0], k)] = "#"
        else:
            for k in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                field[(k, start[1])] = "#"
        start = end

# Find the min/max of the interested dimensions
max_y = 0
min_x = 10000000
max_x = 0
for (x,y) in field.keys():
    max_y = max(max_y, y)
    min_x = min(x, min_x)
    max_x = max(x, max_x)


# returns a value if the sand can take any step, or None if not
def step(s, f):
    steps = [(0,1), (-1,1), (1,1)]
    for i in steps:
        if (s[0] + i[0], s[1] + i[1]) not in f:
            return (s[0] + i[0], s[1] + i[1])
    return None


# make the piles
searching = True
while searching:
    prv = (500,0)
    nxt = step(prv, field)
    while nxt is not None:
        prv = nxt
        nxt = step(prv, field)
        if prv[1] > max_y:
            searching = False
            break
    field[prv] = 'o'
field.__delitem__(prv) # the last one in this round 'fell off the edge'
print("1:", list(field.values()).count('o')) # the result

# make the bottom floor
for i in range(min_x - 200, max_x + 200):
    field[(i, max_y + 2)] = '#'

# continue the pile - no need to restart
searching = True
while searching:
    prv = (500,0)
    nxt = step(prv, field)
    while nxt is not None:
        prv = nxt
        nxt = step(prv, field)
    field[prv] = 'o'
    if prv == (500,0):
        break

print("2:", list(field.values()).count('o')) # the result
