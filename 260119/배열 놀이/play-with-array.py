N, Q = map(int, input().split())
find = list(map(int, input().split()))
q_list = [list(map(int, input().split())) for _ in range(Q)]

for i in range(Q):
    question = q_list[i][0]
    if question == 1:
        idx = q_list[i][1]
        print(find[idx-1])
    elif question == 2:
        ans = q_list[i][1]
        if ans in find:
            for x in range(len(find)):
                if find[x] == ans:
                    print(x+1)
                    break
        else:
            print(0)
    elif question == 3:
        s_idx = q_list[i][1]
        e_idx = q_list[i][2]
        print(*find[s_idx-1:e_idx])
