N = int(input())

arr = [1, N]
arr = arr + [0] * 7

for i in range(2,9):
    arr[i] = arr[i-2] + arr[i-1]
    if arr[i] < 100:
        continue
    else:
        break

print(*arr)