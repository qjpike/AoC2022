from collections import deque
dat = list(map(str.strip, open('input.txt').readlines()))

f = dict()
s = 0
e = 0
for y, arr in enumerate(dat):
    for x, height in enumerate(arr):
        if height == 'S':
            s = (x,y)
            f[s] = 0
        elif height == 'E':
            e = (x,y)
            f[(x,y)] = ord('z') - ord('a')
        else:
            f[(x,y)] = ord(height) - ord('a')


def find_dist(start, end, field):
    cur_pos = start
    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    queue = deque()
    queue.append(cur_pos)
    steps_field = dict()
    steps_field[cur_pos] = 0
    while cur_pos != end and len(queue):
        cur_pos = queue.popleft()
        for i in moves:
            next = (i[0] + cur_pos[0], i[1] + cur_pos[1])
            if next in field:
                if field[next] <= field[cur_pos] + 1:
                    if next not in steps_field:
                        queue.append(next)
                    elif steps_field[next] > steps_field[cur_pos] + 1:
                        queue.append(next)

                    if next in steps_field:
                        steps_field[next] = min(steps_field[cur_pos] + 1, steps_field[next])
                    else:
                        steps_field[next] = steps_field[cur_pos] + 1

    if end in steps_field:
        return steps_field[end]
    else:
        return 10000000


print("1:", find_dist(s, e, f) )

# probably a better way to do part 2. Takes a few seconds.
# my guess is that we have to go from E backwards.
q = deque()
for k,v in f.items():
    if v == 0:
        q.append(tuple(k))

m = 100000000000
for i in q:
    # print(i, find_dist(i,e,f))
    m = min(find_dist(i, e, f), m)

print("2:", m)