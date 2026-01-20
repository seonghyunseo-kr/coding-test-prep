n = int(input())
a = list(map(int, input().split()))


if a[0] > a[1]:
    first, second = a[0], a[1]
else:
    first, second = a[1], a[0]

for i in range(2, n):
    if a[i] > first:
        second = first
        first = a[i]
    elif a[i] > second:
        second = a[i]

print(first, second)
