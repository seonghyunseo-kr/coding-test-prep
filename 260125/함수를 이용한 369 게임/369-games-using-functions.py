a, b = map(int, input().split())

# 자릿수 별 숫자 나누는 함수
def counter(a, b):
    total_cnt = 0
    for num in range(a, b+1):
        if num % 3 != 0:
            num = list(str(num))
            div_cnt = 0
            for i in num:
                if i == '3' or i == '6' or i == '9':
                    div_cnt += 1
            if div_cnt > 0:
                total_cnt += 1 
        else:
            total_cnt += 1

    print(total_cnt)

counter(a, b)

