n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
arr = []
for word in str:
    if word[0:len(t)] == t:
        arr.append(word)

sorted_arr = sorted(arr)
print(sorted_arr[k-1])

