N = int(input())

# Please write your code here.
def program(N):
    if N == 1:
        return 2
    
    if N == 2:
        return 4 
    
    return (program(N-1) * program(N-2)) % 100 

print(program(N))