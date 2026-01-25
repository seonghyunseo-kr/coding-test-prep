A, B = map(int, input().split())

for j in range(2, 10, 2):
    row = [f"{i} * {j} = {i * j}" for i in range(B, A - 1, -1)]
    print(*row, sep=' / ')
print()