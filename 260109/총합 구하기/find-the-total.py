A, B = map(int, input().split())

ans = 0 
for i in range(A, B+1):
    if i % 6 == 0 and i % 8 != 0:
        ans += i

print(ans)