arr = list(map(int, input().split()))
cnt = [0] * 10

for x in arr:
    if x == 0:
        break
    tens = (x // 10) % 10
    cnt[tens] += 1

for i in range(1, 10):
    print(i, '-', cnt[i])