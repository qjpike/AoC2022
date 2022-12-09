dat = list(map(str.split, open("input.txt").readlines()))


def touching(h, t):
    return abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2


def m_dist(h, t):
    return abs(h[0] - t[0]) + abs(h[1] - t[1])


def move(point, dir):
    if dir == 'U':
        point = (point[0], point[1] + 1)
    elif dir == 'R':
        point = (point[0] + 1, point[1])
    elif dir == "D":
        point = (point[0], point[1] - 1)
    elif dir == "L":
        point = (point[0] - 1, point[1])
    else:
        print("*****Well, We've fucked up boys****")
        exit()
    return point


def diag_follow(h, t):
    if abs(h[0] - t[0]) > 1:
        return (t[0] + (h[0] - t[0]) // abs(h[0] - t[0]), t[1] + (h[1] - t[1]) // abs(h[1] - t[1]))
    if abs(h[1] - t[1]) > 1:
        return (t[0] + (h[0] - t[0]) // abs(h[0] - t[0]), t[1] + (h[1] - t[1]) // abs(h[1] - t[1]))


def straight_follow(h, t):
    if abs(h[0] - t[0]) > 1:
        return (t[0] + (h[0] - t[0]) // abs(h[0] - t[0]), t[1])
    else:
        return (t[0], t[1] + (h[1] - t[1]) // abs(h[1] - t[1]))


snake = [(0,0)] * 10
p2_visited = set()
p1_visited = set()
for i in dat:
    for j in range(int((i[1]))):
        prev_head = snake[0]
        snake[0] = move(snake[0], i[0])

        for k in range(len(snake[:-1])):
            head = snake[k]
            tail = snake[k+1]

            if not touching(head, tail):
                if m_dist(head, tail) < 3:
                    snake[k+1] = straight_follow(head, tail)
                else:
                    snake[k+1] = diag_follow(head, tail)
                p2_visited.add(snake[-1])
                prev_head = tail
            else:
                break
        p1_visited.add(snake[1])
    # for y in range(-5, 20):
    #     for x in range(-12, 20):
    #         if (x,y) in snake:
    #             print(snake.index((x,y)),end='')
    #         elif (x,y) == (0,0):
    #             print("s",end='')
    #         else:
    #             print(".",end='')
    #     print(" ")
    # print("********************************************************")
    # print("-------------------------------------------------------")

print("1:", len(p1_visited))
print("2:", len(p2_visited))
