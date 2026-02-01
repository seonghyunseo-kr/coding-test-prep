n = int(input())

OFFSET = 101
MAX_R = OFFSET * 2
blocks = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for i in range(n):
    x1, y1 = map(int, input().split())
    x2, y2 = x1 + 8, y1 + 8 
    for r in range(x1, x2):
        for c in range(y1, y2):
            blocks[r][c] = 1

ans = 0 
for row in blocks:
    ans += sum(row)
print(ans)