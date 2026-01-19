arr = list(map(int, input().split()))
n = len(arr)

for i in range(n):
    if arr[i] % 3 == 0:
        print(arr[i-1])
        break