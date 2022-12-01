
def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            if i == '\n':
                inp.append(0)
            else:
                inp.append(int(i))

    return inp

dat = get_input()
counts = []
curr_sum = 0
for i in dat:
    if i == 0:
        counts.append(curr_sum)
        curr_sum = 0
    else:
        curr_sum += i

counts.sort()
print("1:", counts[-1])
print("2:", sum(counts[-3:]))
