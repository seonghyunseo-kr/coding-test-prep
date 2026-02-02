n, m = map(int, input().split())

OFFSET = 1000001
MAX_D = OFFSET * 2 + 1
a_dist = [0] * MAX_D
b_dist = [0] * MAX_D

# Process robot A's movements
curr_time = 1
for _ in range(n):
    time, dir = input().split()
    time = int(time)
    if dir == 'R':
        for _ in range(time):
            a_dist[curr_time] = a_dist[curr_time-1] + 1
            curr_time += 1
    else:
        for _ in range(time):
            a_dist[curr_time] = a_dist[curr_time-1] - 1
            curr_time += 1

total_time_a = curr_time - 1

# Process robot B's movements
curr_time = 1
for _ in range(m):
    time, dir = input().split()
    time = int(time)
    if dir == 'R':
        for _ in range(time):
            b_dist[curr_time] = b_dist[curr_time-1] + 1
            curr_time += 1
    else:
        for _ in range(time):
            b_dist[curr_time] = b_dist[curr_time-1] - 1
            curr_time += 1

total_time_b = curr_time - 1

total_time = max(total_time_a, total_time_b)
for i in range(total_time_a + 1, total_time + 1):
    a_dist[i] = a_dist[total_time_a]
for i in range(total_time_b + 1, total_time + 1):
    b_dist[i] = b_dist[total_time_b]

ans = 0 
for i in range(1, total_time+1):
    if a_dist[i] == b_dist[i] and a_dist[i-1] != b_dist[i-1]:    
        ans += 1

print(ans)