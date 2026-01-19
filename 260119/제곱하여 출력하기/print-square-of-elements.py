N = int(input())
arr = list(map(int, input().split()))

new_arr = [elem ** 2 for elem in arr]
print(*new_arr)