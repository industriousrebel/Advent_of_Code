#%%
m_num =  277678  + 1
    
# %%
import math
from collections import deque
size = math.ceil(math.sqrt(m_num))*2
# %%
matrix = [[0 for k in range(size)] for i in range(size)]
moves = [(0,1),(1,0),(0,-1),(-1,0)]
m = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
sx = size//2
sy = size//2
max_sx,max_sy,s,m_idx,n_size  = 0,0,0,0,0

counter_against = max_sx
for i in range(1,m_num):

    if n_size > counter_against:
        m_idx = (m_idx + 1) % len(moves)
        if m_idx in (0,2):
            counter_against = max_sx
            max_sx +=1
        else:
            counter_against = max_sy
            max_sy +=1
        n_size = 0
    # print(s,moves[m_idx],counter_against,n_size,m_idx,s)
    sx,sy = sx + moves[m_idx][0],sy + moves[m_idx][1]
    if i <= 1:
        start_pt = (sx,sy)
        matrix[sy][sx] = i
    else:
        for j in m:
            matrix[sy][sx] += matrix[sy + j[1]][sx + j[0]]
    if matrix[sy][sx] > m_num:
        print(matrix[sy][sx])
        break
    n_size += 1
# %%
final_ans = abs(sx - start_pt[0]) + abs(sy - start_pt[1])
# %%

# %%
matrix[start_pt[1]][start_pt[0]]
# %%
