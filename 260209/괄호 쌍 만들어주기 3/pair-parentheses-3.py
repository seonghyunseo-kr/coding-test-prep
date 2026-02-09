A = list(input())

# Please write your code here.
cnt = 0 
for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] != A[j] and A[i] == '(':
            cnt += 1
print(cnt)
