n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# Please write your code here.

def match(start, end, a, b):
    if a[start:end] == b:
        return True

yes_cnt = 0
for i in range(n1-n2+1):
    if match(i, i+n2, a, b) == True:
        yes_cnt += 1

if yes_cnt > 0:
    print('Yes')
else:
    print('No')