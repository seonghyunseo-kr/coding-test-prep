N = int(input())
arr = list(map(int, input().split()))

ans = []
for i in range(N):
    if arr[i] % 2 ==0:
        ans.append(arr[i])
print(*ans)