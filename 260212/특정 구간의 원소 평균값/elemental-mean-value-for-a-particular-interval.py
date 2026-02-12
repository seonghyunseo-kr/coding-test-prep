n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0 
for i in range(n):
    for j in range(i, n):
        sum_val = sum(arr[i:j+1])
        cnt_val = len(arr[i:j+1])
        
        if cnt_val != 0:
            mean_val = sum_val / cnt_val 
        else:
            continue

        if mean_val in arr[i:j+1]:
            cnt += 1

print(cnt)