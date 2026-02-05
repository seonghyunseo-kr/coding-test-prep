n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 1-based index를 유지하기 위해 1 ~ n 범위를 체크합니다.
def in_range(x, y, n):
    return 1 <= x <= n and 1 <= y <= n

# 방향 설정: R, D, U, L
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = mapper[d]

for _ in range(t):
    # 다음 이동할 위치를 미리 계산
    nr, nc = r + dxs[move_dir], c + dys[move_dir]
    
    if in_range(nr, nc, n):
        # 격자 안이라면 그대로 이동
        r, c = nr, nc
    else:
        # 격자 밖이라면 방향만 반대로 바꿈 (이동은 하지 않음, 1초 소모)
        move_dir = 3 - move_dir

print(r, c)