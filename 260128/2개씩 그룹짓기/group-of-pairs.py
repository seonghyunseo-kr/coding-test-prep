n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
max_val = 0
nums.sort()
for i in range(n):
    curr_max = nums[i] + nums[2*n - 1 - i]

    if curr_max > max_val:
        max_val = curr_max

print(max_val)