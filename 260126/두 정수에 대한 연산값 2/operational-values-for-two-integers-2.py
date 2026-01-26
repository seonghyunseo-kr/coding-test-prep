a, b = map(int, input().split())

# Please write your code here.
def program(a, b):
    if a > b:
        a = a * 2
        b = b + 10
    else:
        a = a + 10 
        b = b * 2
    return a, b

a, b = program(a, b)
print(a, b)

