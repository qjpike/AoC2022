def eval_list(l, r):
    pairs = list(zip(l,r))
    for i, pair in enumerate(pairs):
        if type(pair[0]) == type(pair[1]) == int:
            if pair[0] < pair[1]:
                return True
            elif pair[0] > pair[1]:
                return False
        elif type(pair[0]) == type(pair[1]) == list:
            retVal = eval_list(pair[0], pair[1])
            if retVal != None:
                return retVal
        elif type(pair[0]) == list:
            retVal = eval_list(pair[0], [pair[1]])
            if retVal != None:
                return retVal
        elif type(pair[1]) == list:
            retVal = eval_list([pair[0]], pair[1])
            if retVal != None:
                return retVal

    if len(r) > len(l):
        return True
    elif len(l) > len(r):
        return False
    else:
        return None


inp = open('input.txt').read().split("\n\n")

count = 0
for idx, i in enumerate(inp):
    left = eval(i.split("\n")[0])
    right = eval(i.split("\n")[1])

    next_val = eval_list(left, right)
    if next_val:
        count += idx + 1

print("1:", count) # too high - 7102; too low - 5536

class Packet:
    def __init__(self, inp):
        self.val = inp

    def __lt__(self, other):
        return eval_list(self.val, other.val)

    def __eq__(self, inp):
        return self.val == inp


inp2 = list(map(str.strip, open('input.txt').readlines()))

part2_inp = []
for i in inp2:
    if i != '':
        part2_inp.append(Packet(eval(i)))
part2_inp.append(Packet([[2]]))
part2_inp.append(Packet([[6]]))

part2_inp.sort()
print("2:", (part2_inp.index([[2]]) + 1) * (part2_inp.index([[6]]) + 1))