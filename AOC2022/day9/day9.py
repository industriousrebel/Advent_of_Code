#%%
from collections import defaultdict

# %%
moves = {'U':[0,1],'D':[0,-1],'L':[-1,0],'R':[1,0]}

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
        head_p[0]  += int(moves[move_type][0])
        head_p[1]  += int(moves[move_type][1])
        c = head_p
        for t in tail_p:
            diff1 = c[0]-t[0]
            diff2 = c[1]-t[1]
            # print(c,diff1 + diff2)
            if  abs(diff1) == 2 or abs(diff2) == 2:
                t[0] = int(c[0]) + (int(moves[move_type][0]) *-1)
                t[1] = int(c[1]) + (int(moves[move_type][1]) *-1)
            c = (t[0],t[1])
            visited.add(tuple(t))
        print(head_p,tail_p)
        # print(head_p,tail_p)
        # visited.add(tuple(tail_p))
print(len(visited))


# %%
# %%
tail_p

#%%
print(visited)
# %%
