n = int(input())
OFFSET = 1001
MAX_R = OFFSET * 2 

x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a + OFFSET)
    y1.append(b + OFFSET)
    x2.append(c + OFFSET)
    y2.append(d + OFFSET)

# Please write your code here.

blocks = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for i in range(n):
    if i % 2 == 0:
        for r in range(x1[i], x2[i]):
            for c in range(y1[i], y2[i]):
                blocks[r][c] = 1 # Red
    else:
        for r in range(x1[i], x2[i]):
            for c in range(y1[i], y2[i]):
                blocks[r][c] = 2 # Blue        

ans = 0
for row in blocks:
    for elem in row:
        if elem == 2:
            ans += 1

print(ans)