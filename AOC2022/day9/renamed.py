# %%
moves = {'D':[0,1],'U':[0,-1],'L':[-1,0],'R':[1,0]}

moverus = [i.replace('\n','').split(' ') for i in open('test_day_9.txt').readlines()]
# %%


# %%
visited = set()
head_p = [0,0]
tail_p = [0,0]
tail_p = [[0,0] for i in range(9)]
for move_type, move_dist in moverus:
    print(move_type)
    for i in range(int(move_dist)):
        # print(moves[move_type])
        prev = head_p
        head_p[0]  += int(moves[move_type][0])
        head_p[1]  += int(moves[move_type][1])
        c = head_p
        t = tail_p[0]
        diff1 = c[0]-t[0]
        diff2 = c[1]-t[1]
        prev = t.copy()
        if  abs(diff1) == 2 or abs(diff2) == 2:
            t[0] = int(c[0]) + (int(moves[move_type][0]) *-1)
            t[1] = int(c[1]) + (int(moves[move_type][1]) *-1)
            s = True
        else:
            s = False
        c = (t[0],t[1])
        print('before loop',head_p,tail_p)
        visited.add(tuple(t))
        for t_e in tail_p[1:]:
            if s == True:
                tmp = t_e.copy()
                t_e[0] = prev[0]
                t_e[1] = prev[1] 
                diff1 = prev[0]-tmp[0]
                diff2 = prev[1]-tmp[1]
                # print(t_e,diff1,diff2) 
                if  abs(diff1) >= 2 or abs(diff2) >= 2:
                    t_e[0] = int(prev[0]) + (int(moves[move_type][0]) )
                    t_e[1] = int(prev[1]) + (int(moves[move_type][1]))
                print(t_e,diff1,diff2)
                prev = tmp
        print(head_p,tail_p)

len(visited)
# %%

# %%
