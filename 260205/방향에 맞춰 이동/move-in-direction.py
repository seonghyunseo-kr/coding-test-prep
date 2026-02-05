n = int(input())

x, y = 0, 0
# Please write your code here.
for _ in range(n):
    dir, dist = input().split()
    dist = int(dist)
    if dir == 'E':
        x, y = x + dist, y
    elif dir == 'N':
        x, y = x, y + dist
    elif dir == 'W':
        x, y = x - dist, y 
    else:
        x, y = x, y - dist 

print(x, y)
        