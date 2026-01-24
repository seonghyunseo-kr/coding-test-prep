N, M = map(int, input().split())
exist = False
placed = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
    r, c = tuple(map(int, input().split()))
    placed[r-1][c-1] = i+1

for row in placed:
    print(*row)