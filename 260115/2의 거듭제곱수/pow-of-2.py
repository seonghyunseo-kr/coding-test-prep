N = int(input())

ans = 0

while N > 1:
    N = N // 2  # N을 2로 나눈 몫으로 업데이트
    ans += 1    # 나눈 횟수(지수)를 1씩 증가

print(ans)
