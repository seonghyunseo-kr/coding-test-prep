a, b = map(int, input().split())

# Please write your code here.

def sosu(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True 

cnt = 0
for i in range(a, b+1):
    if sosu(i) == True:
        prod = i // 10
        remainder = i % 10 
        if (prod + remainder) % 2 == 0:
            cnt += 1
print(cnt)