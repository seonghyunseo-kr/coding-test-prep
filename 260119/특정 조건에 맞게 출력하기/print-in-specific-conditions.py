arr = list(map(int, input().split()))

n = len(arr)
new_arr = []

for i in range(n):
    if arr[i] != 0:
        if arr[i] % 2 != 0:
            new_arr.append(arr[i] + 3)
        else:
            new_arr.append(arr[i] // 2)
    else:
        break 
print(*new_arr)