n = int(input())
scores = []

class Score:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, kor, eng, math

for _ in range(n):
    name, kor, eng, math = input().split()
    scores.append(Score(name, int(kor), int(eng), int(math)))

scores.sort(key=lambda x: (x.kor + x.eng + x.math))

for s in scores:
    print(s.name, s.kor, s.eng, s.math)