N = int(input())

for i in range(1, N+1):
    for j in range(N, 0, -1):
        num = i * j
        print(num, end=' ')
    print()
