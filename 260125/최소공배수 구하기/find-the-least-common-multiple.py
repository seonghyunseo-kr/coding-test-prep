n, m = map(int, input().split())

# Please write your code here.
def printer(n, m):
    max_num = max(n, m)
    ans = 1
    for i in range(1, max_num+1):
        if n % i == 0 and m % i == 0:
            ans *= i 
    print(ans)

printer(n, m)