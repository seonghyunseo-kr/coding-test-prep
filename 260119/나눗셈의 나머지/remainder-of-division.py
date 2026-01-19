A, B = map(int, input().split())

remainder = []

while A >= 1:
    remainder.append(A % B) 
    A = A // B 

remainder_cnt = [0] * B
for x in remainder:
    remainder_cnt[x] += 1

ans = 0 
for i in remainder_cnt:
    ans += i ** 2
print(ans)
