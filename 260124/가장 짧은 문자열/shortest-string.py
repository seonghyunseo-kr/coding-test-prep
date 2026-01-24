a = str(input())
b = str(input())
c = str(input())

len_a, len_b, len_c = len(a), len(b), len(c)

max_len = max(len_a, len_b, len_c)
min_len = min(len_a, len_b, len_c)

print(max_len-min_len)