n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
blocks = [0] * n
for (ai, bi) in commands:
    for i in range(ai-1, bi):
        blocks[i] += 1

print(max(blocks))