M, D = map(int, input().split())

# Please write your code here.

def date(M, D):
    if M < 13 and D < 32:
        if M != 2:
            print('Yes')
        else:
            if D < 29:
                print('Yes')
            else:
                print('No')

date(M, D)