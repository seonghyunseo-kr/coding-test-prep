MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Score_Program:
    def __init__(self, name, score):
        self.name = name
        self.score = score

code_score_list = []
for i in range(MAX_N):
    new = Score_Program(codenames[i], scores[i]) # 객체 생성
    code_score_list.append(new)

min_val = code_score_list[0] # 첫 번째 객체를 기준으로 시작
for i in range(1, MAX_N):
    if code_score_list[i].score < min_val.score:
        min_val = code_score_list[i]

print(f"{min_val.name} {min_val.score}")