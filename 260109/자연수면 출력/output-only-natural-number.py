A, B = map(int, input().split())

if A > 0:
    for i in range(1, B+1):
        print(A, end ='')
        i += 1
else:
    print(0)