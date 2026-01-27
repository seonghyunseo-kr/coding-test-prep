N = int(input())

# Please write your code here.
def program(N):
    if N == 0:
        return N

    return program(N//10) + (N % 10) ** 2

print(program(N))
