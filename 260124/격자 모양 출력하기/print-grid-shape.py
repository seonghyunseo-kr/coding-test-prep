N, M = map(int, input().split())
placed = [[0 for _ in range(N)] for _ in range(N)]
exist = False 
for _ in range(M):
    r,c = tuple(map(int, input().split()))
    placed[r-1][c-1] = r * c

for row in placed:
    print(*row)