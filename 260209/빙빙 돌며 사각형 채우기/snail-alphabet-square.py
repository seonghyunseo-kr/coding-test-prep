n, m = map(int, input().split())

# Please write your code here.
def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

grid = [['' for _ in range(m)] for _ in range(n)] # 문자를 채울 예정이므로 빈 리스트로 초기화 

# 우-하-좌-상 순서대로 
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
r, c, dir_num = 0, 0, 0 

current_char_code = ord('A')
grid[r][c] = chr(current_char_code)

for i in range(2, n*m + 1):
    nr, nc = r + dxs[dir_num], c + dys[dir_num]

    if not in_range(nr, nc) or grid[nr][nc] != '':
        dir_num = (dir_num + 1) % 4
        nr, nc = r + dxs[dir_num], c + dys[dir_num]
    
    r, c = nr, nc
    current_char_code = ord('A') + (current_char_code - ord('A') + 1) % 26
    grid[r][c] = chr(current_char_code)

for row in grid:
    print(*row, sep=' ')