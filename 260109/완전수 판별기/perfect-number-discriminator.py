N = int(input())

vals = [] # 약수의 목록
for i in range(1, N+1):
    if N % i == 0:
        vals.append(i)

sum_val = 0 
for i in vals:
    if i != N:
        sum_val += i 

if sum_val == N:
    print('P')
else:
    print('N')