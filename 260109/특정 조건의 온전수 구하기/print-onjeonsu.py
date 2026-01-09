N = int(input())

ans = 0
for i in range(1, N+1):
    if i % 2 == 0 or i % 5 == 0 or (i % 3 == 0 and i % 9 != 0):
        ans += 0 
    else:
        print(i, end=' ')