A, B = map(int, input().split())

ans_list = []
if A < B:
    ans_list.append(1)
else:
    ans_list.append(0)

if A == B:
    ans_list.append(1)
else:
    ans_list.append(0)

print(*ans_list)