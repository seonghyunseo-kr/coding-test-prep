N = int(input())

cnt = 2

for i in range(N):
    for j in range(N):
        if cnt < 10:
            print(cnt, end=' ')
        else:
            cnt = 2
            print(cnt, end=' ')
        cnt += 2
    print()