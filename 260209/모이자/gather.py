n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
import sys
INT_MAX = sys.maxsize

min_dist = INT_MAX
for i in range(n):
    sum_dist = 0 
    for j in range(n):
        sum_dist += abs(j-i) * A[j]
    
    min_dist = min(min_dist, sum_dist)

print(min_dist)