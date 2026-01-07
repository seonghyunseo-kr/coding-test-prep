h, w = map(int, input().split())
b = round(((10000 * w) / (h * h)), 1)

print(int(b))

if b >= 25:
    print('Obesity')
