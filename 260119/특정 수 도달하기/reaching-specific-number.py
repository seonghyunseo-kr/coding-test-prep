arr = list(map(int, input().split()))

sum_val = 0
cnt = 0 

for i in arr:
    if i < 250:
        sum_val += i 
        cnt += 1
    else:
        break 

mean_val = sum_val / cnt 
print(sum_val, f"{mean_val:.1f}", sep=' ')