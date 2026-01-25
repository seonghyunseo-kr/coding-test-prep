y = int(input())

# Please write your code here.
def decider(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            print('false') # 평년 
        else:
            print('true') # 윤년
    else:
        print('false') # 평년 

decider(y)