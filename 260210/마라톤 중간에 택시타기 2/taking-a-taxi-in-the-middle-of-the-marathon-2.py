n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
OFFSET = 1001
MAX_R = OFFSET * 2 + 1

min_dist = 1000000

for i in range(1, n-1): # 맨 처음과 맨 마지막은 제외하고 건너 뛸 체크포인트 확인
    new_points = points[:i] + points[i+1:] # j만 제외

    dxs = [p[0] for p in new_points]
    dys = [p[1] for p in new_points]

    dist = 0 

    for i in range(len(new_points)-1):
        x1, y1 = dxs[i], dys[i]
        x2, y2 = dxs[i+1], dys[i+1]

        dist += abs(x1-x2) + abs(y1-y2)

    if dist < min_dist:
        min_dist = dist

print(min_dist)

