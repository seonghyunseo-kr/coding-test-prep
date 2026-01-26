N = int(input())

# Please write your code here.
def program(N):
    if N == 0:
        return

    program(N-1)
    print("HelloWorld")

program(N)