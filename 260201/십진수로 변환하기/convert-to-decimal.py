binary = input()

# Please write your code here.
binary = list(binary)
num = 0
for i in range(len(binary)):
    binary[i] = int(binary[i])
    num = num * 2 + binary[i]
    
print(num)
