n = int(input())

arr = []
cnt = 0 

for i in range(1, 11) :
    val = n * i
    arr.append(n*i)

    if val % 5 == 0:
        cnt += 1

    if cnt >= 2:
        break 
    
print(*arr)