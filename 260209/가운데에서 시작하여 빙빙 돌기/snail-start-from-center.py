n = int(input())
grid = [[0] * n for _ in range(n)]

# 우-상-좌-하
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
r, c, dir_num = n // 2, n // 2, 0
grid[r][c] = 1

curr_num = 2 # 이미 1이 채워진 초기값 다음에 이동해야 할 번호 부여 
move_num = 1 # 이동해야 할 칸 수

# n*n까지 숫자를 채울 때까지 반복
while curr_num <= n * n:
    # 한 세트(두 번의 방향 전환)마다 이동 거리가 일정함 (e.g., 1칸씩 두 번 or 2칸씩 두 번 움직임)
    for _ in range(2):
        # 현재 방향(dir_num)으로 move_num만큼 실제로 전진!
        for _ in range(move_num):
            if curr_num > n * n: # 모든 칸을 다 채웠으면 종료
                break
            
            r, c = r + dxs[dir_num], c + dys[dir_num]
            
            if 0 <= r < n and 0 <= c < n:
                grid[r][c] = curr_num
                curr_num += 1
        
        # move_num만큼 가고 나서 방향을 꺾음
        dir_num = (dir_num + 1) % 4
        
    # 두 번 방향을 꺾었으므로 다음엔 한 칸 더 많이 가야 함
    move_num += 1

for row in grid:
    print(*row)
