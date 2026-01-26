A = input()

def palindrome(A):
    new_list = []
    for i in range(len(A)-1, -1, -1):
        new_list.append(A[i])
    
    reversed_A = "".join(new_list)
    
    if reversed_A == A:
        print("Yes")
    else:
        print("No")

palindrome(A)
