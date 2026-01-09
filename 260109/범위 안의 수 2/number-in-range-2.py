num = [int(input()) for _ in range(10)]

sum_val, sum_val_cnt = 0, 0 
for i in num:
    if i >= 0 and i <=200:
        sum_val += i 
        sum_val_cnt += 1
mean_val = sum_val / sum_val_cnt

print(sum_val, f"{mean_val:.1f}", sep=' ')