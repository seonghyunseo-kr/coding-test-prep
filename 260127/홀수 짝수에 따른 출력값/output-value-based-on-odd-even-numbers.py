N = int(input())

# Please write your code here.
def program(N):
    if N == 1:
        return 1
    if N == 2:
        return 2

    if N % 2 == 0:
        return program(N-2) + N
    else:
        return program(N-2) + N

print(program(N))