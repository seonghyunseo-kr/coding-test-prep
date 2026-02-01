n = int(input())

OFFSET = 10000
blocks = [0] * (OFFSET * 2 + 1)
last_color = [0] * (OFFSET * 2 + 1)

curr = OFFSET
for _ in range(n):
    x, dir = input().split()
    x = int(x)

    if dir == 'R':
        start, end = curr, curr + x - 1
        for i in range(start, end + 1):
            blocks[i] += 1
            last_color[i] = 2 # Black
        curr = end 
    else:
        start, end = curr - x + 1, curr
        for i in range(start, end + 1):
            blocks[i] += 1
            last_color[i] = 1 # White
        curr = start

w_ans, b_ans= 0, 0
for i in range(OFFSET * 2 + 1):
    if last_color[i] == 1:
        w_ans += 1
    elif last_color[i] == 2: 
        b_ans += 1

print(w_ans, b_ans)