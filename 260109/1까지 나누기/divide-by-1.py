N = int(input())

cnt = 0
divisor = 1  

while N > 1:
    N = N // divisor
    cnt += 1
    divisor += 1  

print(cnt)
