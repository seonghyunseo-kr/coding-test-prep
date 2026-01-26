n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]


# Please write your code here.
def program():
    global arr
    
    for i in range(m):
        a1, a2 = queries[i]
        new_arr = arr[a1-1:a2]
        sum = 0
        for j in new_arr:
            sum += j 
        print(sum)

program()