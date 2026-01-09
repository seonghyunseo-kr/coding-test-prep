B, A = map(int, input().split())
i = B
while i >= A:
    if i % 2 == 0:
        print(i, end=' ')
    i -= 1