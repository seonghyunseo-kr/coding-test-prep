n = int(input())

OFFSET = 100
MAX_R = 200
blocks = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range (x1, x2):
        for j in range(y1, y2):
            blocks[i][j] = 1

area = 0
for row in blocks:
    area += sum(row)

print(area)