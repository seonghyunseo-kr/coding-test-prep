N = int(input())
nums = list(map(int, input().split()))

min_diff = None
for i in range(N-1):
    if nums[i] > nums[i+1]:
        diff = nums[i] - nums[i+1]
    else:
        diff = nums[i+1]-nums[i]
    
    if min_diff is None or diff < min_diff:
        min_diff = diff

print(min_diff)