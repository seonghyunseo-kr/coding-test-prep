n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
ans = sorted(nums)
print(ans[k-1])