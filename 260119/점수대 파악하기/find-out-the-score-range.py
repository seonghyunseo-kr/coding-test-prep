arr = list(map(int, input().split()))
cnt = [0] * 11

for x in arr:
    if x == 0: 
        break
    
    cnt[x // 10] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {cnt[i]}")
