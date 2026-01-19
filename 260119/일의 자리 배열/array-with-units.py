arr = list(map(int, input().split()))
arr = arr + [0] * 8

for i in range(2, 10):
    arr[i] = (arr[i-1] + arr[i-2]) % 10

print(*arr)