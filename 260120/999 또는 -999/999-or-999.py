N = list(map(int, input().split()))

min_val, max_val = N[0], N[0]
for elem in N:
    if elem == 999 or elem == -999:
        break
    else:
        if elem < min_val:
            min_val = elem
        if elem > max_val:
            max_val = elem

print(max_val, min_val)
    