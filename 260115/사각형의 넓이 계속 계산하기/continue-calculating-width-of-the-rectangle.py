while True:
    r, c, t = input().split()
    r, c = int(r), int(c)

    prod = r * c
    print(prod)

    if t == 'C':
        break