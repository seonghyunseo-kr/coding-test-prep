arr = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    sum_arr = 0
    for j in range(4):
        sum_arr += arr[i][j]
    mean_arr = sum_arr/4
    print(mean_arr, end=' ')
print()
for i in range(4):
    sum_arr = 0
    for j in range(2):
        sum_arr += arr[j][i]
    mean_arr = sum_arr / 2
    print(mean_arr, end=' ')
print()

sum_arr = 0 
for i in range(2):
    for j in range(4):
        sum_arr += arr[i][j]
mean_arr = sum_arr / 8 
print(mean_arr)