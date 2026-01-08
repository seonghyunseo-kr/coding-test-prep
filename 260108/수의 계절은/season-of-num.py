M = int(input())

if M >= 3 and M <= 5:
    print('Spring')
elif M >= 6 and M <= 8:
    print('Summer')
elif M >= 9 and M <= 11:
    print('Fall')
elif M >=12 or M <=2:
    print('Winter')