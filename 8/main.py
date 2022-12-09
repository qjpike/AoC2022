dat = []

with open("input.txt") as f:
    for i in f.readlines():
        dat.append(list(map(int, i.strip())))

visible_trees = set()
y_highest = [-1] * len(dat[0])
for y, i in enumerate(dat):

    x_pos_max = -1
    for x, x_height in enumerate(i):
        if x_height > x_pos_max:
            x_pos_max = x_height
            visible_trees.add((x,y))
        if x_height > y_highest[x]:
            y_highest[x] = x_height
            visible_trees.add((x, y))

dat.reverse()
y_highest = [-1] * len(dat[0])
for y, i in enumerate(dat):
    i.reverse()
    x_pos_max = -1
    for x, x_height in enumerate(i):
        if x_height > x_pos_max:
            x_pos_max = x_height
            visible_trees.add((len(i) - x - 1,len(dat) - y - 1))
        if x_height > y_highest[x]:
            y_highest[x] = x_height
            visible_trees.add((len(i) - x - 1,len(dat) - y - 1))
print("1:", len(visible_trees))


dat = []

with open("input.txt") as f:
    for i in f.readlines():
        dat.append(list(map(int, i.strip())))


max_visible = 0
for y, row in enumerate(dat):

    for x, curr_height in enumerate(row):
        score = 1
        visible = 0
        x_pos_max = -1
        for next_height in row[x+1:]:
            if next_height < curr_height:
                visible += 1
            else:
                visible += 1
                break
        score *= visible
        visible = 0
        for next_height in reversed(row[:x]):
            if next_height < curr_height:
                visible += 1
            else:
                visible += 1
                break
        score *= visible
        visible = 0
        for next_height in dat[y+1:]:
            if next_height[x] < curr_height:
                visible += 1
            else:
                visible += 1
                break
        score *= visible
        visible = 0
        for next_height in reversed(dat[:y]):
            if next_height[x] < curr_height:
                visible += 1
            else:
                visible += 1
                break
        score *= visible
        max_visible = max(max_visible, score)


print("2:", max_visible)
