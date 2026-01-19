arr = list(map(int, input().split()))
n = len(arr)

cnt_arr = [0] * n 
for elem in arr:
    num = elem //  10 
    cnt_arr[num] += 1

for i in range(1, n):
    cnt = cnt_arr[i]
    print(i, '-', cnt)