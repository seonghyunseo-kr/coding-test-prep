m1, d1, m2, d2 = map(int, input().split())

dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

is_reversed = False
if (m1, d1) > (m2, d2):
    m1, d1, m2, d2 = m2, d2, m1, d1
    is_reversed = True

elapsed_days = 0
curr_m, curr_d = m1, d1

while not (curr_m == m2 and curr_d == d2):
    elapsed_days += 1
    curr_d += 1
    if curr_d > dates[curr_m]:
        curr_m += 1
        curr_d = 1

if is_reversed:
    result_index = (0 - elapsed_days) % 7
else:
    result_index = (0 + elapsed_days) % 7

print(days[result_index])