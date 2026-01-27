n = int(input())
arr = list(map(int, input().split()))

def get_max(n, arr):
    # 기저 조건: 원소가 하나뿐이라면 그 원소가 최댓값
    if n == 1:
        return arr[0]
    
    prev_max = get_max(n - 1, arr)
    
    if arr[n - 1] > prev_max:
        return arr[n - 1]
    else:
        return prev_max

print(get_max(n, arr))
