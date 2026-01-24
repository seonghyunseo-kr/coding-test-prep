N = int(input())
ans = []
for i in range(N):
    arr = [1 for _ in range(i+1)]
    ans.append(arr)

for i in range(2, N):
    for j in range(1, i):
        ans[i][j] = ans[i-1][j-1] + ans[i-1][j]

for row in ans:
    print(*row)