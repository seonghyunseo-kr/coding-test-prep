N = int(input())

# 1. 초기 항 설정
arr = [1, N]

# 2. 마지막에 추가된 항(arr[-1])이 100 이하인 동안 계속 반복
while arr[-1] <= 100:
    # 전전항(arr[-2])과 전항(arr[-1])을 더해 새로운 값을 만듦
    next_val = arr[-1] + arr[-2]
    # 리스트에 추가
    arr.append(next_val)

# 3. 전체 수열 출력
print(*arr)
