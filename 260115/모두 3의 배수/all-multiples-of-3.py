num = [int(input()) for _ in range(5)]

ans = True
for i in num:
    if i % 3 != 0:
        ans = False 

if ans == True:
    print(1)
else:
    print(0)