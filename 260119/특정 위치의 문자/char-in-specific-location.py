word = ['L', 'E', 'B', 'R', 'O', 'S']
idx = -1

w = input()

for i in range(len(word)):
    if word[i] == w:
        idx = i

if w in word:
    print(idx)
else:
    print('None')