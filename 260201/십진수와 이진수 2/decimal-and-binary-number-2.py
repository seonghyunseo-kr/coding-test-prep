N = input()

# Please write your code here.
N = list(N)
num = 0
for i in range(len(N)):
    N[i] = int(N[i])
    num = num * 2 + N[i]

num = num * 17
digits = []
while True:
    if num < 2:
        digits.append(num)
        break
    
    digits.append(num % 2)
    num = num // 2

for d in digits[::-1]:
    print(d, end='')