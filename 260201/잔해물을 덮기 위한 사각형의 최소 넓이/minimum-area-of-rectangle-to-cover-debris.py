x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

OFFSET = 1001
MAX_R = OFFSET * 2 
blocks = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]
x1[0], y1[0], x2[0], y2[0] = x1[0] + OFFSET , y1[0] + OFFSET , x2[0] + OFFSET , y2[0] + OFFSET 
x1[1], y1[1], x2[1], y2[1] = x1[1] + OFFSET , y1[1] + OFFSET , x2[1] + OFFSET , y2[1] + OFFSET 

for r in range(x1[0], x2[0]):
    for c in range(y1[0], y2[0]):
        blocks[r][c] = 1

for r in range(x1[1], x2[1]):
    for c in range(y1[1], y2[1]):
        blocks[r][c] = 0 

min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0
found = False
for r in range(MAX_R + 1):
    for c in range(MAX_R + 1):
        if blocks[r][c] == 1:
            found = True
            if r < min_x: 
                min_x = r
            if r > max_x: 
                max_x = r
            if c < min_y: 
                min_y = c
            if c > max_y: 
                max_y = c

if found:
    width = (max_x + 1) - min_x
    height = (max_y + 1) - min_y
    print(width * height)

