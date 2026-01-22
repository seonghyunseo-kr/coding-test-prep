n, m = map(int, input().split())

# Please write your code here.
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 1

for i in range(n):
    for j in range(i-1, -1, -1):
        arr[i][j] += num
        num += 1
        print(i, j, arr[i][j])