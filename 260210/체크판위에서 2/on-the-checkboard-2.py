R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
start = grid[0][0]
end= grid[R-1][C-1]

cnt = 0
for r1 in range(1, R):
    for c1 in range(1, C):
        # 1st move
        if start != grid[r1][c1]:
            for r2 in range(r1+1, R-1):
                for c2 in range(c1+1, C-1):
                    # 2nd move 
                    if grid[r2][c2] != grid[r1][c1] and grid[r2][c2] != end:
                        cnt += 1
print(cnt)