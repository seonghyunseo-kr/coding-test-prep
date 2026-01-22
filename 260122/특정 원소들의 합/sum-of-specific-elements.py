arr = [list(map(int, input().split())) for _ in range(4)]
sum_arr = 0
for i in range(4):
    new_arr = arr[i]
    for j in range(0, i+1):
        sum_arr += new_arr[j]

print(sum_arr)