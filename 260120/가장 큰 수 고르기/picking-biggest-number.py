arr = list(map(int, input().split()))

max_val = 0 
for a in arr:
    if a > max_val:
        max_val = a 
print(max_val)
    