a, b, c = map(int, input().split())

cnt = 0

for i in range(a, b+1):
    if i % c == 0:
        cnt += 1
    else:
        cnt += 0 

if cnt != 0:
    print('YES')
else:
    print('NO')