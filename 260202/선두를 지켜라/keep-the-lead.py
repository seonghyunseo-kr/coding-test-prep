n, m = map(int, input().split())

MAX_T = 100001
a_blocks = [0] * MAX_T
b_blocks = [0] * MAX_T

curr_time = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a_blocks[curr_time] = a_blocks[curr_time - 1] + v
        curr_time += 1

curr_time = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b_blocks[curr_time] = b_blocks[curr_time - 1] + v
        curr_time += 1

total_time = curr_time 

leader, ans = 0, 0 # if leader == 1: A is leading / leader == 2: B is leading 
for i in range(total_time):
    if a_blocks[i] > b_blocks[i]:
        if leader == 2:
            ans += 1
        leader = 1
    elif b_blocks[i] > a_blocks[i]:
        if leader == 1:
            ans += 1
        leader = 2

print(ans)