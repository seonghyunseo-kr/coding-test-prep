N = int(input())
ans = []
for i in range(N):
    arr = [1 for _ in range(i+1)]
    ans.append(arr)
    # for j in range(1, i+1):
    #     arr[j] = arr[i-1][j-1] + arr[i-1][j]
    #     # print(i, j, arr[j])

for row in ans:
    print(*row)