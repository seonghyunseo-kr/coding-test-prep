n = int(input())

room, hall, toilet = 0, 0, 0 
for i in range(1, n+1):
    if i % 2 == 0 and i % 3 == 0 and i % 12 == 0:
        toilet += 1
    elif i % 2 == 0 and i % 3 == 0 and i % 12 != 0:
        hall += 1
    elif i % 2 == 0 and i % 3 != 0 and i % 12 == 0:
        toilet += 1
    elif i % 2 != 0 and i % 3 == 0 and i % 12 == 0:
        toilet += 1
    elif i % 2 == 0 and i % 3 != 0 and i % 12 != 0:
        room += 1
    elif i % 2 != 0 and i % 3 == 0 and i % 12 != 0:
        hall += 1
    elif i % 2 != 0 and i % 3 != 0 and i % 12 == 0:
        toilet += 1
    
    
    

print(room, hall, toilet, sep=' ')