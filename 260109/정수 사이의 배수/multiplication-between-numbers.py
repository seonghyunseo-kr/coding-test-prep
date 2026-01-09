A, B = map(int, input().split())

sum_val, sum_val_cnt = 0, 0
for i in range(A, B+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i 
        sum_val_cnt += 1

mean_val = sum_val / sum_val_cnt

print(sum_val, f"{mean_val:.1f}", sep=' ')
