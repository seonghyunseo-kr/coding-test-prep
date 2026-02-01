n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
blocks = [0] * 101
for (s, e) in segments:
    for i in range(s, e+1):
        blocks[i] += 1

print(max(blocks))
