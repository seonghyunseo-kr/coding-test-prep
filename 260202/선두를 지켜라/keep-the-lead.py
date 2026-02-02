n, m = map(int, input().split())

MAX_T = 1000001
a_pos = [0] * MAX_T
b_pos = [0] * MAX_T

curr_time = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a_pos[curr_time] = a_pos[curr_time - 1] + v
        curr_time += 1
total_time = curr_time


curr_time = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b_pos[curr_time] = b_pos[curr_time - 1] + v
        curr_time += 1

# 선두 교체 횟수 계산
leader = 0 # 1: A가 선두, 2: B가 선두, 0: 동점
ans = 0

for i in range(1, total_time):
    if a_pos[i] > b_pos[i]:
        if leader == 2: # 이전에 B가 선두였다면 교체 발생
            ans += 1
        leader = 1
    elif b_pos[i] > a_pos[i]:
        if leader == 1: # 이전에 A가 선두였다면 교체 발생
            ans += 1
        leader = 2

print(ans)
