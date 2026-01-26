n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def divider(a):
    if a % 2 == 0:
        a = int(a / 2)
        print(a, end=' ')
    else:
        print(a, end=' ')

for i in arr:
    divider(i)