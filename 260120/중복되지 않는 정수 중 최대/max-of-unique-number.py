n = int(input())
nums = list(map(int, input().split()))

# 1. 각 숫자가 몇 번 등장했는지 카운트합니다.
count_dict = {}
for x in nums:
    if x in count_dict:
        count_dict[x] += 1
    else:
        count_dict[x] = 1

# 2. 딱 1번만 등장한 숫자들을 골라내어 그중 최댓값을 찾습니다.
max_val = -1 # 중복 없는 숫자가 없을 경우를 대비해 -1로 초기화

for x in count_dict:
    if count_dict[x] == 1: # 중복되지 않은 숫자라면
        if x > max_val:
            max_val = x

print(max_val)
