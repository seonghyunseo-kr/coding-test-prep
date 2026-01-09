num = [int(input()) for _ in range(10)]

cnt3, cnt5 = 0, 0 
for i in num:
    if i % 3 == 0 and i % 5 != 0:
        cnt3 += 1
    elif i % 5 == 0 and i % 3 != 0:
        cnt5 += 1
    elif i % 3 == 0 and i % 5 == 0:
        cnt3 += 1
        cnt5 += 1


print(cnt3, cnt5)