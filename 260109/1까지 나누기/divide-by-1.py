N = int(input())

cnt = 1
for i in range(1, N+1):
    if N / i > 1:
        N = N // i
        cnt += 1
        continue
    else:
        break

print(cnt)