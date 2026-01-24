N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]
num = 1

if N % 2 == 0:
    for i in range(N-1, -1, -1):
        if i % 2 != 0:
            for j in range(N-1, -1, -1):
                arr[j][i] += num
                num += 1
        else:
            for j in range(N):
                arr[j][i] += num
                num += 1
else:
    for i in range(N-1, -1, -1):
        if i % 2 == 0:
            for j in range(N-1, -1, -1):
                arr[j][i] += num
                num += 1
        else:
            for j in range(N):
                arr[j][i] += num
                num += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()