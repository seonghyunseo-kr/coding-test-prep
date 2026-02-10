n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
max_sum = 0 
for i in range(n):
    for j in range(i+2, n):
        sub_sum = 0 
        sub_sum += numbers[i] + numbers[j]
        
        if sub_sum > max_sum:
            max_sum = sub_sum
            
print(max_sum)