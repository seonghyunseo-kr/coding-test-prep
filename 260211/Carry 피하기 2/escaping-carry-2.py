n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def num_divider(num):
    num_div_list = []
    while num > 0:
        remainder = num % 10 
        num = num // 10 
        num_div_list.append(remainder)
    return num_div_list

num_div_list_i = num_divider(int(522))
num_div_list_j = num_divider(int(6))
num_div_list_k = num_divider(int(7311))

def match_list_len(l1, l2, l3):
    max_len = max(len(l1), len(l2), len(l3))
    for lst in (l1, l2, l3):
        while len(lst) < max_len:
            lst.append(0)
    return l1, l2, l3

def carry(l1, l2, l3):
    list_len = len(l1)
    sum_val = 0 
    carry = False 
    for i in range(list_len):
        sum_val = l1[i] + l2[i] + l3[i]
        if sum_val >= 10:
            carry = True
    return carry
    
max_val = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            # print(arr[i], arr[j], arr[k])
            num_div_list_i, num_div_list_j, num_div_list_k = num_divider(arr[i]), num_divider(arr[j]), num_divider(arr[k])
            num_div_list_i, num_div_list_j, num_div_list_k = match_list_len(num_div_list_i, num_div_list_j, num_div_list_k)
            if carry(num_div_list_i, num_div_list_j, num_div_list_k) == False:
                sum_val = arr[i] + arr[j] + arr[k]
                if sum_val > max_val:
                    max_val = sum_val 
            
        
print(max_val)
                