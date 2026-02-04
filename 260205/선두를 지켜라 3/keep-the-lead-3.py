N, M = map(int, input().split())

MAX_T = 1000001
a_blocks = [0] * (MAX_T + 1)
b_blocks = [0] * (MAX_T + 1)

# Process A's movements
curr_time = 0
for _ in range(N):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        a_blocks[curr_time] = a_blocks[curr_time-1] + vi
        curr_time += 1

total_time = curr_time 

# Process B's movements
curr_time = 0
for _ in range(M):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        b_blocks[curr_time] = b_blocks[curr_time-1] + vi
        curr_time += 1

# 명예의 전당
honor = [0] * (total_time) # A = 1, B = 2, A&B = 3
for i in range(total_time):
    if a_blocks[i] > b_blocks[i]:
        honor[i] = 1
    elif a_blocks[i] < b_blocks[i]:
        honor[i] = 2
    else:
        honor[i] = 3

cnt = 0
for i in range(total_time):
    if i == 0 or honor[i] != honor[i-1]:
        cnt += 1

print(cnt)
