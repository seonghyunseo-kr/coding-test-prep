M, D = map(int, input().split())

# Please write your code here.

def date(M, D):
    if M < 8 and M != 2:
        if M % 2 == 0 and D < 31:
            print('Yes')
        elif M % 2 != 0 and D < 32:
            print('Yes')
        else:
            print('No')
    elif M >= 8 and M < 13:
        if M % 2 == 0 and D < 32:
            print('Yes')
        elif M % 2 != 0 and D < 31:
            print('Yes')
        else:
            print('No')
    elif M == 2:
        if D < 29:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

date(M, D)