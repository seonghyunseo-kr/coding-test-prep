n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def program(n, m, A):
    ans = A[m-1]
    while m > 1:
        if m % 2 != 0:
            m = m - 1
            ans += A[m-1]
        else:
            m = int(m / 2)
            ans += A[m-1]
    print(ans)

program(n, m, A)