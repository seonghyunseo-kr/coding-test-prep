a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def plus(a, o, c):
    print(f"{a} {o} {c} = {a + c}")

def minus(a, o, c):
    print(f"{a} {o} {c} = {a - c}")

def prod(a, o, c):
    print(f"{a} {o} {c} = {a * c}")

def divide(a, o, c):
    print(f"{a} {o} {c} = {a // c}")


if o == '+':
    plus(a, o, c)
elif o == '-':
    minus(a, o, c)
elif o == '*':
    prod(a, o, c)
elif o == '/':
    divide(a, o, c)
else:
    print('False')