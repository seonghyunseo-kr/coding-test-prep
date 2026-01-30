n = int(input())

class Program:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

lists = []
for _ in range(n):
    name, height, weight = input().split()
    lists.append(Program(name, int(height), int(weight)))

lists.sort(key=lambda x: (x.height, -x.weight))

for l in lists:
    print(l.name, l.height, l.weight)