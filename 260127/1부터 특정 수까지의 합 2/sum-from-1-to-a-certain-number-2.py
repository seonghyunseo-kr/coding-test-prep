N = int(input())

# Please write your code here.
def program(N):
    if N == 1:
        return 1
    
    return program(N-1) + N


print(program(N))