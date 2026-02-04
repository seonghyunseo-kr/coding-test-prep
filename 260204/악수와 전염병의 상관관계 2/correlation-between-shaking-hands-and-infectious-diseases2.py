N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

n_shake = [K] * N 
contaminated = [0] * N 
contaminated[P-1] = 1

handshakes.sort(key=lambda x: x[0])

for i in range(T):
    t, x, y = handshakes[i]
    
    # 1. 악수 시작 시점의 감염 여부를 미리 저장 
    x_was_infected = contaminated[x-1]
    y_was_infected = contaminated[y-1]

    # 2. x가 감염자고 횟수가 남았다면 y를 감염시키고 횟수 차감
    if x_was_infected == 1 and n_shake[x-1] > 0:
        contaminated[y-1] = 1
        n_shake[x-1] -= 1
        
    # 3. y가 감염자고 횟수가 남았다면 x를 감염시키고 횟수 차감
    # (이미 위에서 x가 감염되었더라도 y_was_infected 기준이라 정확히 횟수가 깎임)
    if y_was_infected == 1 and n_shake[y-1] > 0:
        contaminated[x-1] = 1
        n_shake[y-1] -= 1

print(*contaminated, sep='')