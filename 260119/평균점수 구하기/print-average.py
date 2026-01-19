score = list(map(float, input().split()))

mean_score = sum(score) / len(score)
print(f"{mean_score:.1f}")