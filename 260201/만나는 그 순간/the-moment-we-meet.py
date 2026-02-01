n, m = map(int, input().split())

# Please write your code here.
OFFSET = 1001
MAX_R = OFFSET * 2 + 1

a_blocks = [0] * MAX_R
b_blocks = [0] * MAX_R

start = 0
for _ in range(n):
    d, t = input().split()
    t = int(t)

    if d == 'R':
        end = t + start
        for i in range(start, end):
            a_blocks[i] = a_blocks[i-1] + 1
        start = end
    else:
        end = t + start
        for i in range(start, end):
            a_blocks[i] = a_blocks[i-1] - 1
        start = end

start = 0
for _ in range(m):
    d, t = input().split()
    t = int(t)

    if d == 'R':
        end = t + start
        for i in range(start, end):
            b_blocks[i] = b_blocks[i-1] + 1
        start = end
    else:
        end = t + start
        for i in range(start, end):
            b_blocks[i] = b_blocks[i-1] - 1
        start = end


ans = 0 
for i in range(1001):
    if a_blocks[i] == b_blocks[i]:
        ans = i + 1
        break
    else:
        ans = -1

print(ans)
