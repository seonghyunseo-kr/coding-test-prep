N, T = map(int, input().split())
str = list(input())
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

# 상-우-하-좌 (북-동-남-서)
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
# 좌표 - 가운데서 시작 / 방향 - 위쪽 보고 시작 (북쪽)
r, c, dir_num = N//2, N//2, 0

ans_sum = board[r][c]

for i in range(T):
    if str[i] == 'L': # 시계 반대 방향으로 방향만 전환 (nr, nc, board[nr][nc]는 그대로 유지)
        dir_num = (dir_num+3) % 4

    elif str[i] == 'R': # 시계 방향으로 방향만 전환 (nr, nc, board[nr][nc]는 그대로 유지)
        dir_num = (dir_num+1) % 4

    else:  # str[i] == 'F': 현재 방향 기준으로 이동 / 이동한 곳의 board[nr][nc]값을 ans_sum에 추가 / 방향 전환 X
        nr, nc = r + dxs[dir_num], c + dys[dir_num] 
        if in_range(nr, nc): # 만약 이동한 좌표가 범위 내라면 
            r, c = nr, nc
            ans_sum += board[r][c]
        else:
            pass 
        
print(ans_sum)