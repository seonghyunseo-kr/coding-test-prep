a = tuple(map(str, input().split()))
b = tuple(map(str, input().split()))

print(*a, *b, sep='')