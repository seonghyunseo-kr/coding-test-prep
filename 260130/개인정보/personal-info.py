n = 5

class Program:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

lists = []
for _ in range(n):
    name, height, weight = input().split()
    lists.append(Program(name, int(height), float(weight)))

lists.sort(key=lambda x: x.name)
print('name')
for l in lists:
    print(l.name, l.height, f"{l.weight:.1f}")

print()

lists.sort(key=lambda x: -x.height)
print('height')
for l in lists:
    print(l.name, l.height, f"{l.weight:.1f}")


