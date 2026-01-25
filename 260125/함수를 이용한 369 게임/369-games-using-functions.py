a, b = map(int, input().split())

# Please write your code here.
def printer(a, b):
    cnt = 0 
    for i in range(a, b+1):
        prod = i // 10
        remainder = i % 10 
        if i % 3 == 0 or prod % 3 == 0 or remainder % 3 == 0:
            cnt += 1
    print(cnt)

printer(a, b)