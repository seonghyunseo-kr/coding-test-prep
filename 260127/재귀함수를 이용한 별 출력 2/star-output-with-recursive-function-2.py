n = int(input())

# Please write your code here.
def program(n):
    if n == 0:
        return
    
    print('* ' * n, sep=' ', end='\n')
    program(n-1)
    print('* ' * n, sep=' ', end='\n')

program(n)