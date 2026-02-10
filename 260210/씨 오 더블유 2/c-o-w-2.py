N = int(input())
S = input()

# Please write your code here.
cnt = 0
for i in range(N):
    if S[i] == 'C':
        for j in range(i+1, N):
            if S[j] == 'O':
                for k in range(j+1, N):
                    if S[k] == 'W':
                        cnt += 1

print(cnt)