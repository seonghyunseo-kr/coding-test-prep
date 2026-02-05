dirs = input()

# Please write your code here.
dirs = list(dirs)
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 1
x, y = 0, 0
for i in range(len(dirs)):
    if dirs[i] == 'L':
        dir_num = (dir_num + 1) % 4
    elif dirs[i] == 'R':
        dir_num = (dir_num + 3) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)