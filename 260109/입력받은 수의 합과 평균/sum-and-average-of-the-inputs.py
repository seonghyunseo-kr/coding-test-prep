N = int(input())
num = [int(input()) for _ in range(N)]

sum_val, sum_val_cnt = 0, 0 
for i in num:
    sum_val += i 
    sum_val_cnt += 1
mean_val = sum_val / sum_val_cnt

print(sum_val, f"{mean_val:.1f}", sep=' ')