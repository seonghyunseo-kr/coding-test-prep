board = [list(map(int, input().split())) for _ in range(19)]

# 가로, 세로, 우하향, 우상향
dr, dc = [0, 1, 1, -1], [1, 0, 1, 1]

def in_range(r, c):
    return 0 <= r < 19 and 0 <= c < 19

def find_winner():
    for r in range(19):
        for c in range(19):
            if board[r][c] == 0:
                continue
            
            color = board[r][c]

            for i in range(4):
                # 전 칸 확인 - 6목이 되는 경우가 있는지 확인 
                prev_r, prev_c = r - dr[i], c - dc[i]
                if in_range(prev_r, prev_c) and board[prev_r][prev_c] == color:
                    continue

                cnt = 1
                nr, nc = r + dr[i], c + dc[i]
                # 앞 칸 확인 - 계속 같은 색이 나올때까지 반복 
                while in_range(nr, nc) and board[nr][nc] == color:
                    cnt += 1
                    nr += dr[i]
                    nc += dc[i]

                # 정확히 같은 색 반복이 5번인 경우만 승리 인정 / 승리한 색, 가운데 좌표 출력 
                if cnt == 5:
                    mid_r = r + dr[i] * 2
                    mid_c = c + dc[i] * 2
                    return color, mid_r + 1, mid_c + 1
                    
    return 0, -1, -1

ans, win_r, win_c = find_winner()
print(ans)
if ans != 0:
    print(win_r, win_c)
