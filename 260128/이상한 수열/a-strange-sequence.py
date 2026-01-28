N = int(input())

# Please write your code here.
def program(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    
    return program(N//3) + program(N-1)

print(program(N))