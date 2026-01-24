N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]
num = 1
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        arr[i][j] += num
        num += 1
        print(i, j, num)


for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()