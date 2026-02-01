n = int(input())
OFFSET = 1000
blocks = [0] * (OFFSET * 2 + 1)

b_cnt = [0] * (OFFSET * 2 + 1)
w_cnt = [0] * (OFFSET * 2 + 1)
g_cnt = [0] * (OFFSET * 2 + 1)

order = [0] * (OFFSET * 2 + 1)

curr = OFFSET
for _ in range(n):
    x, dir = input().split()
    x = int(x)

    if dir == 'R':
        start, end = curr, curr + x - 1
        for i in range(start, end+1):
            blocks[i] += 1 
            b_cnt[i] += 1 
            order[i] = 'B'
        curr = end
    else:
        start, end = curr - x + 1, curr
        for i in range(start, end+1):
            blocks[i] += 1
            w_cnt[i] += 1
            order[i] = 'W'
        curr = start
    
for i in range(len(blocks)):
    if blocks[i] >= 4 :
        if b_cnt[i] >= 2 and w_cnt[i] >= 2:
            order[i] = 'G'

w, b, g = 0, 0, 0
for o in order:
    if o == 'W':
        w += 1
    elif o == 'B':
        b += 1
    elif o == 'G':
        g += 1
print(w, b, g)