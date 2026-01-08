M, F = map(int, input().split())

if M >= 90:
    if F >=95:
        s = 100000
    elif F >= 90:
        s = 50000
    else:
        s = 0 
else:
    s = 0

print(s)