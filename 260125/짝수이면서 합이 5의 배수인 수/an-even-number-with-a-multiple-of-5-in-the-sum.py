n = int(input())

# Please write your code here.
def printer(n):
    prod = n // 10 
    remainder = n % 10 
    if n % 2 == 0 and (prod+remainder) % 5 == 0:
        print('Yes')
    else:
        print('No')

printer(n)