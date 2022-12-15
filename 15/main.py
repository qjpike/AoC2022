def m_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def count_row(row, f):
    amts = set()
    y_row = row
    for s, d in f.items():
        x_pos = s[0]
        y_pos = s[1]
        if abs(y_pos - y_row) < d:
            delta = d - abs(y_pos - y_row)
            amts = amts.union(set(list(range(x_pos - delta, x_pos + delta))))

    return len(amts)


def find_range(y, f):
    range_max = 4000000
    ranges = []
    for p, d in f.items():
        if m_dist(p, (p[0], y)) < d:
            delta = d - m_dist(p, (p[0],y))
            ranges.append((max(p[0] - delta, -1),min(p[0] + delta, range_max + 1)))
    idx = 0
    ranges.sort()
    for b,e in ranges:
        if b <= idx <= e:
            idx = e + 1
    if idx < 4000000:
        return idx
    return False


dat = list(map(str.split, open("input.txt").readlines()))
field = dict()
for i in dat:
    s = (int(i[2][2:-1]), int(i[3][2:-1]))
    b = (int(i[8][2:-1]), int(i[9][2:]))
    field[s] = m_dist(s,b)

print("1:", count_row(2000000, field))

# slow but it works. Much faster running from m->0
m = 4000000
for y in range(m, 0, -1):
    result = find_range(y, field)
    if result:
        print("2:", result*m + y)
        break
