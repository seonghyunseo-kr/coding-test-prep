a, b = map(int, input().split())

# Please write your code here.
def is_onjeonsu(num):
    if num % 2 == 0:
        return False
    if num % 10 == 5:
        return False
    if num % 3 == 0 and num % 9 != 0:
        return False
    return True 

cnt = 0
for i in range(a, b+1):
    if is_onjeonsu(i) == True: 
        cnt += 1

print(cnt)
