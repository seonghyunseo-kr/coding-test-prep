N = int(input())
nums = [int(input()) for _ in range(N)]

for i in nums:
    if i % 2 != 0 and i% 3 == 0:
        print(i, end='\n')