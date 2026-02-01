n, m = map(int, input().split())

MAX_T = 1000001
a_blocks = [0] * MAX_T
b_blocks = [0] * MAX_T

curr_time = 0
for _ in range(n):
    d, t = input().split()
    t = int(t)

    for _ in range(t):
        curr_time += 1
        if d == 'R':
            a_blocks[curr_time] = a_blocks[curr_time - 1] + 1
        else:
            a_blocks[curr_time] = a_blocks[curr_time - 1] - 1

total_time_a = curr_time


curr_time = 0
for _ in range(m):
    d, t = input().split()
    t = int(t)
    for _ in range(t):
        curr_time += 1
        if d == 'R':
            b_blocks[curr_time] = b_blocks[curr_time - 1] + 1
        else:
            b_blocks[curr_time] = b_blocks[curr_time - 1] - 1

total_time_b = curr_time

total_time = max(total_time_a, total_time_b)

for i in range(total_time_a + 1, total_time + 1):
    a_blocks[i] = a_blocks[total_time_a]
for i in range(total_time_b + 1, total_time + 1):
    b_blocks[i] = b_blocks[total_time_b]


ans = -1
for i in range(1, total_time + 1):
    if a_blocks[i] == b_blocks[i]:
        ans = i
        break

print(ans)