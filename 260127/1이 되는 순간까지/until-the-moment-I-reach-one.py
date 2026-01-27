N = int(input())

# Please write your code here.
def program(N):
    if N < 2:
        return 0

    if N % 2 == 0:
        return program(N // 2) + 1
    else:
        return program(N // 3) + 1

print(program(N))