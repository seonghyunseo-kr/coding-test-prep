n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

def in_range(x, y):

    return 0 <= x < n and 0 <= y < m

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0
dir_num = 0
arr[x][y] = 1 

for i in range(2, n * m + 1):
    # 1. 다음으로 갈 칸을 일단 계산해봄
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    # 2. 만약 그 칸이 격자를 벗어나거나 이미 숫자가 있다면
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        # 방향을 90도 회전
        dir_num = (dir_num + 1) % 4
        # 3. 회전한 방향으로 다시 갈 칸을 계산
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    # 4. nx, ny로 이동
    x, y = nx, ny
    arr[x][y] = i 


for row in arr:
    print(*row)