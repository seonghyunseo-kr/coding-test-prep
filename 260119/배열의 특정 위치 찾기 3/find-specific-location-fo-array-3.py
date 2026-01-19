arr = list(map(int, input().split()))

ans_list = []
for i in arr:
    if i != 0:
        ans_list.append(i)
    else:
        break

print(sum(ans_list[-3:]))