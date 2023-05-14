#%%
data = list(map(lambda x: [(list(map(int,x[0].split(',')))),list(map(int,(x[1].split(','))))]
,[i[len('Sensor at x='):].replace('\n','')
.replace(', y=',',')
.split(': closest beacon is at x=')[:] for i in  open('test.txt').readlines()]))
# %%
data

# %%
x_co = []
y_co = []
for i in data:
    x_co += [i[0][0],i[1][0]]
    y_co += [i[0][1],i[1][1]]


# %%
x_co = sorted(x_co)
y_co = sorted(y_co)
print(x_co,y_co)
#%%P
# %%
grid = [['.']*(abs(x_co[0])+abs(x_co[-1])+1) for i in range(y_co[0],y_co[-1]+1)]
for i in data:
    x_diff = abs(x_co[0]) if x_co[0] < 0 else 0
    print(x_diff)
    print(i[1][0]+2,i[1][1]-1)
    grid[i[1][1]][i[1][0]+x_diff] = 'B'
    grid[i[0][1]][i[0][0]+x_diff] = 'S'

# %%
for idx,i in enumerate(grid):
    print(idx,''.join(i))
# %%
len(grid[0])
# %%
