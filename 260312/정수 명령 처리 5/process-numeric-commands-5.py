N = int(input())

command = []
num = []
ans = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back":
        num.append(int(line[1]))
    elif line[0] == "get":
        get_num = int(line[1])
        ans.append(num[get_num-1])
    elif line[0] == 'size':
        ans.append(len(num))
    elif line[0] == 'pop_back':
        num.remove(num[-1])

# print answer 
print(*ans, sep='\n', end='\n')