student = int(input())
score = [input().split() for _ in range(student)]

pf_cnt = 0 

for i in range(student):
    sum_val = 0 
    for j in range(4):
        sum_val += int(score[i][j])

    mean_val = sum_val / 4 
    if mean_val >= 60:
        print('pass')
        pf_cnt += 1
    else:
        print('fail')

print(pf_cnt)
    
