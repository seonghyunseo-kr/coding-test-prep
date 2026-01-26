n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def program(n, arr):
    for i in range(n):
        arr[i] = abs(arr[i])
    return arr

arr = program(n, arr)
print(*arr)