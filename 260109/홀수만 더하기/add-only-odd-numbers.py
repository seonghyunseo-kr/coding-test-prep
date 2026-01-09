N = int(input())
num = [int(input()) for _ in range(N)]

ans = 0 
for i in num:
    if i % 2 != 0 and i % 3 == 0:
        ans += i 
    
print(ans)