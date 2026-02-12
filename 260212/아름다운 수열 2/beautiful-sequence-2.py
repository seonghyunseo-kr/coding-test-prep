N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

beautiful = 0 
for i in range(N-M+1):
    sub_A = A[i:i+M]
    cnt = 0
    for j in range(M):
        if sub_A[j] in B:
            cnt += 1

        if cnt == M:
            beautiful += 1

print(beautiful)