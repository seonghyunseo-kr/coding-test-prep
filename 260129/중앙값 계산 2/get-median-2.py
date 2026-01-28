n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(1, n+1):
    if i % 2 != 0:
        new_arr = arr[0:i]
        sorted_new_arr = sorted(new_arr)
        median_idx = (i//2) 

        print(sorted_new_arr[median_idx], end=' ')

