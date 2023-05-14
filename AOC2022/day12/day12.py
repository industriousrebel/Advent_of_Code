#%%
from collections import deque
data =  [[c for c in i.replace('\n','')] for i in  open('Input.txt').readlines() ]
# %%
min_len = len(data)*len(data[0])
## FORMAT FOR BFS, queue, visited, distance/level/sum prev + next
def func(start,min_len):
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    it = start
    q = deque()
    vis = set()
    q.append(it)
    vis.add(it)
    distance = [ [0]*len(data[0]) for i in range(len(data))]

    while q:
        it = q.popleft()
        for move in moves:
            new_iter = (it[0] + move[0], it[1] + move[1])
            if new_iter[0] >= 0 and new_iter[0] < len(data) and new_iter[1] >= 0 and new_iter[1] < len(data[0]):
                if  ord(data[new_iter[0]][new_iter[1]]) -  ord(data[it[0]][it[1]]) <= 1:
                    if new_iter not in vis:
                        vis.add(new_iter)
                        q.append(new_iter)
                        distance[new_iter[0]][new_iter[1]] = distance[it[0]][it[1]] + 1 #Level increase.

    if distance[target[0]][target[1]] != 0:
        print(distance[target[0]][target[1]])
        return distance[target[0]][target[1]]
    else:
        return 0

# %%
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'E':
            target = (i,j)
            data[i][j] = 'z'
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'S' or data[i][j] == 'a' :
            start = (i,j)
            data[i][j] = 'a'
            ret = func(start,min_len)
            if ret != 0:
                min_len = min(min_len,ret)
# %%
min_len
# %%
