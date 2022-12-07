class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.files = dict()
        self.subfolders = dict()
        self.size = 0
        self.parent = parent

    def __str__(self):
        return self.name

    def add_file(self, fname, fsize):
        self.files[fname] = fsize

    def add_subfolder(self, fname):
        self.subfolders[fname] = Folder(fname)

    def find_size(self):
        for i in self.files.values():
            self.size += i
        for i in self.subfolders.values():
            self.size += i.find_size()
        return self.size


dat = []
with open("input.txt") as f:
    for i in f.readlines():
        dat.append(i.split())


cur_folder = top_folder = Folder('/', None)
for i in dat:
    if i[0].isnumeric():
        cur_folder.files[i[1]] = int(i[0])
    elif i[0] == 'dir':
        cur_folder.subfolders[i[1]] = Folder(i[1], cur_folder)
    elif i[0] == '$' and i[1] == 'cd':
        if i[2] == '..':
            cur_folder = cur_folder.parent
        elif i[2] == '/':
            continue
        else:
            cur_folder = cur_folder.subfolders[i[2]]

from collections import deque

top_folder.find_size()

next = deque(top_folder.subfolders.values())
small_folders = []
best_folder = 40000000000000
needed = 30000000 - (70000000 - top_folder.size)
while len(next) > 0:
    temp = next.popleft()
    if temp.size <= 100000:
        small_folders.append(temp.size)
    next += temp.subfolders.values()
    if needed < temp.size < best_folder:
        best_folder = temp.size
print(sum(small_folders))
print(best_folder)