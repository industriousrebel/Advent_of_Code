#%%
import re
input = [i.replace('\n','') for i in open('input.txt').readlines()]
d = {}
for i in input:
    print(i.split(' => ')[0].split('/'),i.split(' => ')[1].split('/'))
    d[tuple(tuple(list(k)) for k in i.split(' => ')[0].split('/'))] = i.split(' => ')[1].split('/')
d
#%%
start = [list(i) for i in 
'''.#.
..#
###'''.split('\n')]
size  = len(start)
#%%
def rotate(grid):
    ## Rotate 90 degrees clockwise *Don't understand this*
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid)-1,-1,-1)]
def flip(grid):
    return [i[::-1] for i in grid]
# %%
if size % 3== 0:
    print(start)
    #Split grid into 3s
elif size % 2 == 0:
    print(start)
    #split grid into 2s 
# %%

counter = 1
temp = start
#%%
temp = rotate(temp)
print(start,temp)
temp == start
# %%
