N1, N2 = map(int, input().split())
A = list(map(int, input().split())) # len(A) == N1
B = list(map(int, input().split())) # len(B) == N2

cnt = 0
for i in range(N2+2):
    start = i 
    end = N2 + i
    if end > N1:
        break

    if A[start:end] == B:
        print("Yes")
        break
    else:
        cnt += 1
        continue

if cnt >= N2+1:
    print('No')
        

