cnt = [0] * 4
e_cnt = 0

for _ in range(3):
    s, tmp = input().split()
    tmp = int(tmp)

    if s == 'Y' and tmp >= 37:
        result = 'A'
        cnt[0] += 1
        e_cnt += 1
    elif s == 'Y' and tmp < 37:
        result = 'C'
        cnt[2] += 1
    elif s == 'N' and tmp >= 37:
        result = 'B'
        cnt[1] += 1
    elif s == 'N' and tmp < 37:
        result = 'D'
        cnt[3] += 1

if e_cnt >= 2:
    print(*cnt, 'E', sep=' ')
else:
    print(*cnt)