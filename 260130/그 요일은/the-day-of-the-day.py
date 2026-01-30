m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
dates = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day_idx = 0
for i in range(len(days)):
    if A == days[i]:
        day_idx = i # A 요일의 인덱스 번호 

elasped_dates = 0
day = 0 
cnt = 0 
while True:
    if m1 == m2 and d1 == d2:
        break
    
    elasped_dates += 1
    d1 += 1
    day += 1

    if d1 > dates[m1]:
        d1 = 1
        m1 += 1

    if day > 6:
        day = 0

    if day == day_idx:
        cnt += 1

print(cnt)