N = int(input())
arr = list(map(int, input().split()))

reverse_arr = []
for i in arr:
    if i % 2 == 0:
        reverse_arr.append(i)
print(*reverse_arr[::-1])