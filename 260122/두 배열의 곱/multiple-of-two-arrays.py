arr1 = [list(map(int, input().split())) for _ in range(3)]
input()
arr2 = [list(map(int, input().split())) for _ in range(3)]

prod = 1
for i in range(3):
    for j in range(3):
        prod = arr1[i][j] * arr2[i][j]
        print(prod, end=" ")
    print()