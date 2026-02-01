n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

OFFSET = 100
MAX_R = 200
blocks = [0] * (MAX_R + 1)

for (x1, x2) in segments:
    start, end = x1 + OFFSET, x2 + OFFSET

    for i in range(start, end):
        blocks[i] += 1
    
print(max(blocks))