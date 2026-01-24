N = int(input())

for i in range(1, 2*N+1, 2):
    for j in range(1, 2*N+1, 2):
        num = 9 + i + j
        print(num, end=' ')
    print()
