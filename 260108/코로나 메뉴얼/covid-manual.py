status1, tmp1 = input().split()
status2, tmp2 = input().split()
status3, tmp3 = input().split()

status1, status2, status3 = str(status1), str(status2), str(status3)
tmp1, tmp2, tmp3 = int(tmp1), int(tmp2), int(tmp3)

def checker(status, tmp):
    if status == 'Y' and tmp >=37:
        check = 'A'
    elif status == 'N' and tmp >=37:
        check = 'B'
    elif status == 'Y' and tmp < 37:
        check = 'C'
    elif status == 'N' and tmp < 37:
        check = 'D'    
    return check 

check1 = checker(status1, tmp1)
check2 = checker(status2, tmp2)
check3 = checker(status3, tmp3)

if check1 == 'A':
    if check2 == 'A' or check3 == 'A':
        print('E')
    else:
        print('N')
else:
    if check2 == 'A' and check3 =='A':
        print('E')
    else:
        print('N')
