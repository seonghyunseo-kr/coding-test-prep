A, B = map(int, input().split())

for j in range(1, 10):
    # 한 줄에 출력될 항목들을 리스트 컴프리헨션으로 생성
    row = [f"{i} * {j} = {i * j}" for i in range(B, A - 1, -1) if i % 2 == 0]
    
    if row:
        print(*row, sep=' / ')
