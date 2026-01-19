arr = list(map(int, input().split()))

odd_sum, even_sum = 0, 0 
n = len(arr)

for i in range(0, n, 2):
    odd_sum += arr[i]

for i in range(1, n, 2):
    even_sum += arr[i] 

if odd_sum > even_sum:
    print(odd_sum-even_sum)
else:
    print(even_sum-odd_sum)