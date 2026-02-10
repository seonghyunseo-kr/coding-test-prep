a = input()

# Please write your code here.
a = list(a)
max_N =0 
for i in range(len(a)):

    new_a = a.copy()
    N = 0 
    # change ith number 
    if new_a[i] == '0':
        new_a[i] = '1'
    else:
        new_a[i] = '0'

    for j in range(len(a)):
        new_a[j] = int(new_a[j])
        multiplier = len(a)-j-1

        N += new_a[j] * (2 ** multiplier)

    if N > max_N:
        max_N = N

print(max_N)

        
