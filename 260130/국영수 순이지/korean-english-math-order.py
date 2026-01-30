# Please write your code here.
n = int(input())
students = []

class Student:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, kor, eng, math

for _ in range(n):
    name_i, kor_i, eng_i, math_i = input().split()
    students.append(Student(name_i, int(kor_i), int(eng_i), int(math_i)))

students.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for s in students:
    print(s.name, s.kor, s.eng, s.math)
