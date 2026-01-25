a, b = map(int, input().split())

# 자릿수 별 숫자 나누는 함수
def divider(a, b):
    for num in range(a, b+1):
        num = list(str(num))
        cnt = 0
        print('num:', num)
        for i in num:
            print('i:', i, end=' ')
            if i == '3' or i == '6' or i == '9':
                cnt += 1
                print(cnt)
    # print(cnt)

divider(a, b)

# # 실제 문제 풀이하는 함수 - count
# def printer(a, b):
#     cnt = 0
#     for i in range(a, b+1):
#         if i % 3 == 0:
#             cnt += 1
#         else:
#             if divider(a, b) == True:
#                 cnt += 1
#     print(cnt)

# printer(a, b)