a, b = map(int, input().split())
n = input()

# a진수 n --> 10진수
n = list(n)
num = 0
for i in range(len(n)):
    n[i] = int(n[i])
    num = num * a + n[i]

digits = []
while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num = num // b

for d in digits[::-1]:
    print(d, end='')