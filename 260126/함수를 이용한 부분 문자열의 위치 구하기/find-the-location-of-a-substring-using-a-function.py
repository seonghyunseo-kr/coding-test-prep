text = input()
pattern = input()

# Please write your code here.
def program(text, pattern):
    text = list(text)
    pattern = list(pattern)
    for i in range(0, len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            ans_idx = i 
            break
        else:
            ans_idx = -1
    print(ans_idx)
    
program(text, pattern)