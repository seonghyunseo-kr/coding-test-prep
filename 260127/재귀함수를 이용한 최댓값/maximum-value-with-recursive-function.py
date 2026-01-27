n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def program(n, arr):
    if n == 0:
        return arr[0]
    
    if arr[n-1] > arr[n-2]:
        max_val = arr[n-1]
        program(n-1, arr) 
    else:
        max_val = arr[n-2]
        program(n-1, arr) 
        
    return max_val

max_val = program(n-1, arr)
print(max_val)