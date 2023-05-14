#%%
import sys
sys.path.insert(1, '/Users/saeed/Desktop/Programming/AOC2017/day10')
from day10 import return_hash
inp1 = 'hxtvlmkl'
# inp1 = 'flqrgnkx' #Test Input
counter = 0
grid = [['.']*128 for i in range(128)]
for r in range(0,128):
    hexxx = return_hash(f'{inp1}-{r}')
    s = ''
    for h in hexxx:
        t  = bin(int(h, 32))[2:].zfill(4)
        s += t
    
    for i in range(len(s)):
        if s[i] == '1':
            grid[r][i] = '#'
            counter += 1
# for i in grid:
#     print(''.join([str(j) for j in i]))

moves = [[0,1],[0,-1],[1,0],[-1,0]]
num_of_regions = 0
def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '.':
        return
    grid[i][j] = '.'
    for move in moves:
        dfs(grid, i + move[0], j + move[1])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            dfs(grid, i, j)
            num_of_regions += 1

print(f'Part 1{counter} and Part 2 {num_of_regions}')


# %%
# %%
