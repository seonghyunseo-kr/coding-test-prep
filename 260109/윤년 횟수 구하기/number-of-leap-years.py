N = int(input())

cnt = 0 
for i in range(1, N+1):
    if i % 4 == 0:
        if i % 100 == 0 and i % 400 != 0:
            cnt += 0
        else:
            cnt += 1
    else:
        cnt += 0 

print(cnt)