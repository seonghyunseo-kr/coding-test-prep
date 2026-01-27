N = int(input())

# Please write your code here.
def program(N):
    if N == 0:
        return

    print(N, end=' ')
    program(N-1)
    print(N, end=' ')

program(N)