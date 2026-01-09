A, B = map(int, input().split())

start = min(A, B)
end = max(A, B)

sum_val = 0 
for i in range(start, end+1):
    if i % 5 == 0:
        sum_val += i

print(sum_val)