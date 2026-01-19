arr = list(map(int, input().split()))

n = len(arr)

even_sum_val = 0
for i in range(1, n, 2):
    even_sum_val += arr[i]

sum_val = 0
cnt = 0
for i in range(2, n, 3):
    sum_val += arr[i]
    cnt += 1
mean_val = round(sum_val / cnt, 1)

print(even_sum_val, mean_val, sep=' ')