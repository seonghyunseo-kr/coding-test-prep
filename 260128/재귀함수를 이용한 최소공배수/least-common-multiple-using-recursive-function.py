# 1. 최대공약수(GCD)를 구하는 함수 (유클리드 호제법)
def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)

# 2. 두 수의 최소공배수(LCM)를 구하는 함수
def get_lcm(a, b):
    return (a * b) // get_gcd(a, b)

# 3. 리스트 전체의 최소공배수를 구하는 재귀 함수
def program(n, arr):
    # 기저 조건: 원소가 하나 남으면 그 값이 최소공배수
    if n == 1:
        return arr[0]
    
    # [재귀적 접근]
    # '현재 마지막 원소'와 '나머지 앞부분의 최소공배수'를 다시 최소공배수 구함
    return get_lcm(arr[n-1], program(n-1, arr))

n = int(input())
arr = list(map(int, input().split()))

print(program(n, arr))
