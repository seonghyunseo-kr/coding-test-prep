A, B = map(int, input().split())

while A <= B:
    print(A, end=' ')
    if A % 2 != 0:
        A = A * 2
    else:
        A = A + 3
    