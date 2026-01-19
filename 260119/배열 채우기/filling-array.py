arr = list(map(int, input().split()))
reverse_arr = []
for i in arr:
    if i == 0:
        break
    else:
        reverse_arr.append(i)

print(*reverse_arr[::-1])