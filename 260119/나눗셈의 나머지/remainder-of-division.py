A, B = map(int, input().split())

remainder = []

while A > 1:
    A = A // B 
    remainder.append(A % B) 

remainder_cnt = [0] * len(remainder)
for x in remainder:
    remainder_cnt[x] += 1

ans = 0 
for i in remainder_cnt:
    ans += i ** 2
print(ans)
