N, M = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0 
for i in range(N):
    if nums[i] == M:
        cnt += 1
print(cnt)