n = int(input())

# Please write your code here.
def program(n):
    if n == 1:
        return 0 
    
    if n % 2 == 0:
        return program(n // 2) + 1
    else:
        return program(n * 3 + 1) + 1

print(program(n))