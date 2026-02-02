n, m = map(int, input().split())

OFFSET = 10001
a_blocks = [0] * OFFSET 
b_blocks = [0] * OFFSET 

# Process A's movements
curr_time = 0
for _ in range(n):
    vi, ti = map(int, input().split())
    dist = vi * ti 
    for i in range(ti):
        curr_time += 1
        if a_blocks[curr_time] == a_blocks[curr_time-1]:
            a_blocks[curr_time] = dist
        else:
            a_blocks[curr_time] = a_blocks[curr_time-1] + dist 

total_time_a = curr_time
    
# Process B's movements
curr_time = 0 
for _ in range(m):
    vi, ti = map(int, input().split())
    dist = vi * ti
    for i in range(ti):
        curr_time += 1
        if b_blocks[curr_time] == b_blocks[curr_time-1]:
            b_blocks[curr_time] = dist
        else:
            b_blocks[curr_time] = b_blocks[curr_time-1] + dist 

total_time_b = curr_time

total_time = max(total_time_a, total_time_b)
for i in range(total_time_a + 1, total_time + 1):
    a_blocks[i] = a_blocks[total_time_a]
for i in range(total_time_b + 1, total_time + 1):
    b_blocks[i] = b_blocks[total_time_b]

ans = 0 
for i in range(total_time):
    if a_blocks[i] == b_blocks[i]:
        ans += 1

print(ans)
