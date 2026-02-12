N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
total_sum = sum(arr)
min_diff = S

for i in range(N):
    for j in range(i+1, N):
        curr_sum = total_sum - arr[i] - arr[j]
        curr_diff = abs(curr_sum - S)

        if curr_diff < min_diff:
            min_diff = curr_diff

print(min_diff)
