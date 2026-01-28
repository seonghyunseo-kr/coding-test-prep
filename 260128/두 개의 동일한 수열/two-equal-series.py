n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
sort_A, sort_B = sorted(A), sorted(B)

if sort_A == sort_B:
    print("Yes")
else:
    print("No")