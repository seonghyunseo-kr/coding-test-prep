A = input()

# Please write your code here.
def program(A):
    A = list(A)
    ans = [A[0]]
    for i in A[1:]:
        if i not in ans:
            ans.append(i)
    if len(ans) >= 2:
        return True 
    else:
        return False

if program(A) == True:
    print('Yes')
else:
    print('No')