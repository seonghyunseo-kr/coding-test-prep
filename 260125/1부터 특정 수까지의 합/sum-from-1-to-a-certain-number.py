n = int(input())

# Please write your code here.
def printer(n):
    sum = 0
    for i in range(1, n+1):
        sum += i 
    ans = sum // 10 
    print(ans)

printer(n)