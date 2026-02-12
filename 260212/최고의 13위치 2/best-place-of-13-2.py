
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 1 * 3 크기의 격자내에 있는 동전 합 구하기 
def get_sum(r, c): 
    return arr[r][c] + arr[r][c+1] + arr[r][c+2]

def is_not_overlapped(r1, c1, r2, c2): # 겹치지 않는 경우를 반환 
    if r1 != r2:
        return True # 같은 행에 있지 않으면 겹치지 않음 
    return abs(c1 - c2) >= 3 # 같은 행에 있는 경우 두 열 값의 차이가 3보다 크거나 같으면 겹치지 않음

max_coins = 0
for r1 in range(n):
    for c1 in range(n-2):
        for r2 in range(n):
            for c2 in range(n-2):
                if is_not_overlapped(r1, c1, r2, c2):
                    current_sum = get_sum(r1, c1) + get_sum(r2, c2)
                    max_coins = max(max_coins, current_sum)

print(max_coins)

