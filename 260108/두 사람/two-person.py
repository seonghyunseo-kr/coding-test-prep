age1, gender1 = input().split()
age2, gender2 = input().split()

age1, age2 = int(age1), int(age2)
gender1, gender2 = str(gender1), str(gender2)

if (age1 >= 19 and gender1 == 'M') or (age2 >= 19 and gender2 == 'M'):
    print(1)
else:
    print(0)