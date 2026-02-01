n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
max_cnt, cnt = 0, 0
for i in range(n):
    if i == 0 or arr[i] > arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)