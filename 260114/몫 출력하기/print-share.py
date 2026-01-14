cnt = 0

while cnt < 3:
    try:
        n = int(input())
    except EOFError:
        break

    if n % 2 == 0:
        print(n // 2)
        cnt += 1