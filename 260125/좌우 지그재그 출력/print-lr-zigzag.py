N = int(input())

num = 1
for i in range(1, N+1):
    if i % 2 != 0:
        for j in range(1, N+1):
            print(num, end=' ')
            num += 1
    else:
        temp_num = num + N - 1
        for j in range(N, 0, -1):
            print(temp_num, end=' ')
            temp_num -= 1
        num += N
    print()