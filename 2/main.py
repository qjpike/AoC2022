dat = []
with open("input.txt") as f:
    for i in f.readlines():
        dat.append(i.split())

score = 0

for i in dat:
    score += ord(i[1]) - ord('W')

    me = ord(i[1]) - ord('X')
    him = ord(i[0]) - ord('A')

    if me - him == 1 or me - him == -2:
        score += 6
    if me - him == 0:
        score += 3

print("1:", score)

vals = [1,2,3]
score = 0
for i in dat:
    him = ord(i[0]) - ord('A')
    command = ord(i[1]) - ord('X')

    if command == 0:
        score += 0
        score += vals[him - 1]
    elif command == 1:
        score += 3
        score += vals[him % 3]
    else:
        score += 6
        score += vals[(him + 1) % 3]

print("2:", score)
