n = int(input())

# Please write your code here.
def printer(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            if num < 10:
                print(num, end=' ')
            else:
                num = 1
                print(num, end=' ')
            num += 1
        print()

printer(n)