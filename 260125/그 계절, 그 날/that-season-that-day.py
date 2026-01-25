Y, M, D = map(int, input().split())

# Please write your code here.
def year(Y):
    if Y % 4 != 0: # 4의 배수가 아니면 윤년 아님 
        return False
    else: # 4의 배수일 때 
        if Y % 100 == 0 and Y % 400 == 0: # 100의 배수면서 400의 배수면 윤년
            return True
        elif Y % 100 != 0 and Y % 400 == 0: # 100의 배수가 아니면 윤년 아님 
            return False
        elif Y % 100 == 0 and Y % 400 != 0: # 100의 배수여도 400의 배수면 윤년 아님
            return False
        else: # 나머지일때는 모두 다 윤년
            return True


def date(Y, M, D):
    if M < 8 and M != 2:
        if M % 2 == 0 and D < 31:
            return True
        elif M % 2 != 0 and D < 32:
            return True
        else:
            return False
    elif M >= 8 and M < 13:
        if M % 2 == 0 and D < 32:
            return True
        elif M % 2 != 0 and D < 31:
            return True
        else:
            return False
    elif M == 2:
        if year(Y) == True:
            if D < 30:
                return True
            else:
                return False
        else:
            if D < 29:
                return True
            else:
                return False 
    else:
        return False

if date(Y, M, D) == True:
    if M >= 3 and M <= 5:
        print('Spring')
    elif M >= 6 and M <= 8:
        print('Summer')
    elif M >= 9 and M <= 11:
        print('Fall')
    elif M == 12 or M <= 2:
        print('Winter')
else:
    print(-1)