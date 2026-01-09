N, a = map(int, input().split())

i = 1
while i <= N:
    if i % a == 0:
        print(1, end='\n')
    else:
        print(0, end='\n') 
    i += 1