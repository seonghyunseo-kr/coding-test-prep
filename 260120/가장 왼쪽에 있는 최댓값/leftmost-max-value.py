n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_idx = n
while min_idx != 0: # 첫번째 인덱스에 도달하기 전까지 반복
    max_val, max_cnt = 0, 0
    for i in range(len(a)): # 
        # print('max_val, max_cnt, min_idx:', max_val, max_cnt, min_idx)
        if a[i] > max_val:
            max_val = a[i]
            max_cnt += 1
            min_idx = i 
    a = a[:min_idx]
    # print('max_val, max_cnt, min_idx:', max_val, max_cnt, min_idx)
    print(min_idx + 1, end=' ')