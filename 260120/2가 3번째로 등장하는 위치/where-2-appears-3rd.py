N = int(input())
num = list(map(int, input().split()))

cnt = 0 
for n in num:

    if n == 2:
        cnt += 1

    if cnt == 3:
        print(num[n]+1)
        break