n = int(input())

OFFSET = 10
blocks = [0] * (OFFSET * 2 + 1)

curr = OFFSET 
for _ in range(n):
    dist, dir = input().split()
    dist = int(dist)

    if dir == 'R':
        start, end = curr, curr + dist
        for i in range(start, end):
            blocks[i] += 1
        curr = end 
    else:
        start, end = curr - dist, curr
        for i in range(start, end):
            blocks[i] += 1
        curr = start 

count = 0
for b in blocks:
    if b >= 2:
        count += 1

print(count)