a, b = map(int, input().split())


print(f"{a // b}.", end="")

remainder = a % b
for _ in range(20):
    remainder *= 10
    print(remainder // b, end="")
    remainder %= b