N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
cnt = [K] * N
ans = 0

for i in range(M):
    s = student[i]
    cnt[s-1] -= 1

    if cnt[s-1] == 0:
        break
    else:
        ans = -1

for i in range(N):
    if cnt[i] == 0 :
        ans = i + 1

print(ans)
