
dat = []
with open("input.txt") as f:
    for i in f.readlines():
        dat.append(i.strip())

score = 0
for i in dat:
    front = i[:len(i)//2]
    back = i[len(i)//2:]

    front_set = set()
    for j in front:
        front_set.add(j)
    back_set = set()
    for j in back:
        back_set.add(j)

    both = back_set.intersection(front_set)
    for j in list(both):
        if j.isupper():
            score += 26 + ord(j) - ord('A') + 1
        else:
            score += ord(j) - ord('a') + 1
print("1:", score)

score = 0
for i in range(0, len(dat), 3):
    first_set = set()
    second_set = set()
    third_set = set()
    for j in dat[i]:
        first_set.add(j)
    for j in dat[i+1]:
        second_set.add(j)
    for j in dat[i+2]:
        third_set.add(j)

    temp = first_set.intersection(second_set)
    temp2 = temp.intersection(third_set)

    for j in list(temp2):
        if j.isupper():
            score += 26 + ord(j) - ord('A') + 1
        else:
            score += ord(j) - ord('a') + 1

print("2:", score)
