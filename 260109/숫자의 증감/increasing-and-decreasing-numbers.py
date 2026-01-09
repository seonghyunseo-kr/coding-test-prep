C, N = input().split()
N = int(N)

if C == 'A':
    for i in range(1, N+1):
        print(i, end=' ')
        i += 1
elif C == 'D':
    for i in range(N, 0, -1):
        print(i, end=" ")
        i -= 1
        