N = int(input())

for i in range(1, N+1):
    if i % 3 == 0:
        print(0, end=' ')
    else:
        if i < 10:
            print(i, end=' ')
        else:
            ten_num = i // 10 # 십의 자리 수는 10으로 나눈 몫에 해당
            one_num = i % 10 # 일의 자리 수는 10으로 나눈 나머지에 해당
            if (ten_num == 3) or (ten_num == 6) or (ten_num == 9) or (one_num == 3) or (one_num == 6) or (one_num == 9):
                print(0, end=' ')
            else:
                print(i, end=' ')