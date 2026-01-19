N = int(input())
arr = list(map(int, input().split()))

cnt_arr = [0] * 10

for elem in arr:
    cnt_arr[elem] += 1

for i in range(1, 10):
    cnt = cnt_arr[i]
    print(cnt)