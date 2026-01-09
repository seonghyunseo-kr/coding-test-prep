N = int(input())

cnt = 0 
for i in range(1, N+1):
    if N / i > 1:
        N = N // i
        cnt += 1
        continue
    else:
        cnt += 1
        break

print(cnt)