a, b, c = map(int, input().split())

ans_list = []
if a == min(a, b, c):
    ans_list.append(1)
else:
    ans_list.append(0)

if a == b and b == c and a == c:
    ans_list.append(1)
else:
    ans_list.append(0)

print(*ans_list)