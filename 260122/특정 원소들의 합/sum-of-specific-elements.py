arr = [list(map(int, input().split())) for _ in range(4)]
print(arr)
sum_arr = 0
for i in range(0, 4, 1):
    for j in range(i):
        sum_arr += arr[i][j]
        print(i, j, arr[i][j], sum_arr)
print(sum_arr)