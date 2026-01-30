n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

dist = []
for idx, (x, y) in points:
    distance = abs(x) + abs(y)
    dist.append((int(idx), int(distance)))

dist.sort(key=lambda x: (x[1], x[0]))

for d in dist:
    print(d[0]+1)