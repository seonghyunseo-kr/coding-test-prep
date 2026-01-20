n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = a[0]
for i in a[1:]:
    if i < min_val:
        min_val = i 

min_cnt = 0
for i in a:
    if min_val == i:
        min_cnt += 1

print(min_val, min_cnt, sep=' ')