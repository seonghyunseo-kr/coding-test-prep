N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

beautiful = 0 
for i in range(N - M + 1):
    sub_A = sorted(A[i : i + M])
    if sub_A == sorted(B):
        beautiful += 1

print(beautiful)