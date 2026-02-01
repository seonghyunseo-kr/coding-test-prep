x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

# x1[0], y1[0], x2[0], y2[0] = map(int, input().split()) # A의 좌표
# x1[1], y1[1], x2[1], y2[1] = map(int, input().split()) # B의 좌표
# x1[2], y1[2], x2[2], y2[2] = map(int, input().split()) # M의 좌표 

# Please write your code here.
OFFSET = 1001
MAX_R = OFFSET * 2
blocks = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for i in range(2):
    x1[i], y1[i], x2[i], y2[i] = map(int, input().split()) # A~M의 좌표 (순서대로 A, B, M)
    for r in range(x1[i], x2[i]):
        for c in range(y1[i], y2[i]):
            blocks[r][c] = 1

x1[2], y1[2], x2[2], y2[2] = map(int, input().split()) # M의 좌표 

for i in range(x1[2], x2[2]):
    for j in range(y1[2], y2[2]):
        blocks[i][j] = 0

ans = 0
for row in blocks:
    ans += sum(row)
print(ans)