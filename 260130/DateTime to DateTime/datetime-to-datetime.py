a, b, c = map(int, input().split())

# Please write your code here.
d, h, m = 11, 11, 11
elasped_time = 0

if a > d and b > h and c > m:
    while True:
        if d == a and h == b and m == c:
            break
        
        elasped_time += 1
        m += 1

        if m == 60:
            h += 1
            m = 0 
        
        if h == 24:
            d += 1
            h = 0
        
    print(elasped_time)
else:
    print(-1)