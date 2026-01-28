a, b, c = map(int, input().split())

# Please write your code here.
num = a * b * c

def program(num):
    if num < 10:
        return num 

    return program(num//10) + (num % 10)

print(program(num))