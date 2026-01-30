n = int(input())
sequence = list(map(int, input().split()))

paired = []
for i, val in enumerate(sequence, start=1):
    paired.append((val, i))

sorted_paired = sorted(paired)

answer = [0] * n
# sorted_paired에는 (값, 원래번호)가 정렬되어 있습니다.
# i+1은 '정렬 후 순위'이고, 
# original_idx는 '원래 몇 번째였는지'입니다.
for i, (val, original_idx) in enumerate(sorted_paired, start=1):
    # 원래 위치(original_idx - 1)에 정렬 순위(i)를 저장합니다.
    answer[original_idx - 1] = i

# 마지막에 한꺼번에 출력
print(*(answer))