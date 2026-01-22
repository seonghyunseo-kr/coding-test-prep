n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

num = 0
for i in range(m):
    # i가 짝수일 때 (0, 2, 4...번째 열): 위에서 아래로 (0 -> n-1)
    if i % 2 == 0:
        for j in range(n):
            arr[j][i] = num
            num += 1
    # i가 홀수일 때 (1, 3, 5...번째 열): 아래에서 위로 (n-1 -> 0)
    else:
        for j in range(n - 1, -1, -1):
            arr[j][i] = num
            num += 1
for row in arr:
    print(*row)
