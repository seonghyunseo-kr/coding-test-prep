N = int(input())
score = list(map(float, input().split()))

mean_score = round(sum(score) / len(score), 1)
print(mean_score)

if mean_score >= 4.0:
    print('Perfect')
elif mean_score >= 3.0:
    print('Good')
else:
    print('Poor')