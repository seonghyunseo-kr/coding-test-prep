board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.

def checker(i, j):
    row, row_cnt = False, 0 # 가로 방향
    col, col_cnt = False, 0 # 세로 방향
    cross, cross_cnt = False, 0 # 대각선 방향

    # 가로 방향 체크 (오른쪽 방향만)
    for k in range(j+1, len(board)-1):
        if board[i][j] == board[i][k] and board[i][k] == board[i][k+1]:
            row_cnt += 1
        else:
            row_cnt = 0 
        if row_cnt == 5:
            print(board[i][k], 'win')
            row = True 
            break

    # 세로 방향 체크 (아래쪽 방향만)
    for l in range(i+1, len(board)-1):
        if board[i][j] == board[l][j] and board[l][j] == board[l+1][j]:
            col_cnt += 1
        else:
            col_cnt = 0 
        if col_cnt == 5:
            print(board[i][k], 'win')
            col = True 
            break 

    # 대각선 방향 체크 (오른쪽-아래 방향만)
    for k in range(j+1, len(board)-1):
        for l in range(i+1, len(board)-1):
            if board[i][j] == board[l][k] and board[l][k] == board[l+1][k+1] and l == k:
                cross_cnt += 1
            else:
                cross_cnt = 0 
            if cross_cnt == 5:
                print(board[i][k], 'win')
                cross = True 
                break 
    return row, col, cross

for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] != 0: # 현재 위치 i, j 

            row, col, cross = checker(i, j) # 현재 위치 기준으로 이후 승리 여부 확인
            print(row, col, cross)

            # 첫번째 줄 - 승리 여부 출력 
            # 두번째 줄 - 연속된 5개 바둑알 중 가운데 위치하고 있는 가로 번호, 세로 번호 
            if row == False and col == False and cross == False: #승리 결정되지 않은 경우 
                print(0)
            else: 
                if board[i][j] == 1: # 검정이 이긴 경우 
                    print(1)
                    print(i+2, j+2) # 연속된 5개 바둑알 중 가운데 위치하고 있는 가로 번호, 세로 번호 
                elif board[i][j] == 2: # 흰색이 이긴 경우 
                    print(2)
                    print(i+2, j+2) # 연속된 5개 바둑알 중 가운데 위치하고 있는 가로 번호, 세로 번호 
            

