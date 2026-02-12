n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_val = 0 
for i in range(n-k+1):
    curr_max_val = 0 
    for j in range(i, i+k):
        curr_max_val += arr[j]
        max_val = max(max_val, curr_max_val)

print(max_val)
    