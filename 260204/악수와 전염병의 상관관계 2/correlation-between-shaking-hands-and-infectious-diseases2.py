N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

# Initialization 
MAX_T = (N * K * T) + 1 
n_shake = [K] * N # n명의 개발자들 각각이 k번 동안만 전염시키는 횟수 기록용 
contaminated = [0] * N # n명의 개발자들 각각의 전염 상태 기록용 
blocks = [0] * MAX_T # 악수하는 t초에 대한 기록 

# 초기 감염자 P 표시
contaminated[P-1] = 1

# handshakes를 t초를 기준으로 정렬 
handshakes.sort(key=lambda x: x[0])

for i in range(T):
    t, x, y = handshakes[i]
    blocks[t] = 1 
    # print(f'{i}번째 악수 조합 시작')
    if i == 0: # 첫번째 순서일 때
        if x == P or y == P: # 첫번째 순서에서 개발자 x 또는 y가 최초 감염자일 때 
            # print(f'개발자 번호 {x}, {y}')
            contaminated[x-1], contaminated[y-1] = 1, 1 # 감염 확인 
            # 개발자들의 악수 횟수 확인 
            n_shake[x-1] -= 1 # 개발자 x의 악수 횟수 차감
            n_shake[y-1] -= 1 # 개발자 y의 악수 횟수 차감
    
    elif i > 0: # 이후 순서일 때 
        # print(f'개발자 번호 {x}, {y}')
        # 새로 악수를 하는 x, y가 이미 감염이 된 상태인지 확인
        if contaminated[x-1] == 1 and contaminated[y-1] == 0: # x만 이미 감염되어 있다면
            if n_shake[x-1] > 0: # 악수 시 감염될 수 있다면 
                contaminated[y-1] = 1 # y를 신규 감염자로 등록
            else: # 악수 시 감염될 수 없다면 (더이상 전염시킬 수 없다면)
                contaminated[y-1] = 0 # y는 감염되지 않은 상태 유지 
            n_shake[x-1] -= 1 # 개발자 x의 악수 횟수 차감
            n_shake[y-1] -= 1 # 개발자 y의 악수 횟수 차감

        elif contaminated[x-1] == 0 and contaminated[y-1] == 1: # y만 이미 감염되어 있다면
            if n_shake[y-1] > 0: # 악수 시 감염될 수 있다면 
                contaminated[x-1] = 1 # x를 신규 감염자로 등록
            else: # 악수 시 감염될 수 없다면 (더이상 전염시킬 수 없다면)
                contaminated[x-1] = 0 # x는 감염되지 않은 상태 유지 
            n_shake[x-1] -= 1 # 개발자 x의 악수 횟수 차감
            n_shake[y-1] -= 1 # 개발자 y의 악수 횟수 차감

        
    # print(f"악수 횟수: {n_shake}")


# Final Output 
print(*contaminated, sep='')