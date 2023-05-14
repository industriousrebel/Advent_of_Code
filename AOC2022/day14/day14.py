#%% Part 1.
from collections import defaultdict
from json import loads
data =  [list(map(lambda x: tuple(map(lambda y: int(y.strip()),x.split(','))),i.replace('\n','').split('->'))) for i in  open('input.txt').readlines() ]
# data =  [list(map(lambda x: tuple(map(lambda y: int(y.strip()),x.split(','))),i.replace('\n','').split('->'))) for i in  open('test.txt').readlines() ]

# print(data)
shift = 800
for i in data:
    for j in i:
        shift = min(j[0],shift)
#%%
max_rock_depth = 0
sand_poring = (500,0)
mega = shift - 100
rock_co = []
for i,ele in enumerate(data):
    idx = 0
    start_p = ele[idx]
    while idx < len(ele):
        if start_p[0] == ele[idx][0]:
            for m in range(min(start_p[1],ele[idx][1]),max(start_p[1],ele[idx][1])+1):
                rock_co.append((start_p[0],m))
        else:
            for m in range(min(start_p[0],ele[idx][0]),max(start_p[0],ele[idx][0])+1):
                rock_co.append((m,start_p[1]))
        start_p = ele[idx]
        idx+=1

#%%
mapper = list(map(lambda x: (x[0]-mega,x[1]),rock_co))
tetris = [['.'] * 500 for i in range(0,200)]
# tetris[16][47] = '#'
for i in mapper:
    tetris[i[1]][i[0]] = '#'
    max_rock_depth = max(max_rock_depth,i[1])
tetris[sand_poring[1]][sand_poring[0]-mega] = '+'
moves = [(0,1),(0,-1),(1,0),(-1,0)]
counter = 0
for idx,i in enumerate(tetris[max_rock_depth+ 2]):
    tetris[max_rock_depth+ 2][idx] = '#'

def r_settle(tetris,co_ordinates,counter=0):
    print(max_rock_depth,co_ordinates[1])
    if co_ordinates[0] == max_rock_depth:
        print('reached bottom')
        return True
    mvs = [(1,0),(1,-1),(1,1)]
    for i in mvs:
        co = [co_ordinates[0]+i[0],co_ordinates[1]+i[1]]
        # print(co)
        if co[1] >= 0 or co[1] < len(tetris[0]) or co[0] >= 0 or co[0] < len(tetris):
            if tetris[co[0]][co[1]] == '.' or tetris[co[0]][co[1]] == '~': 
                counter +=1
                tetris[co[0]][co[1]] = '~'
                state = r_settle(tetris,co,counter)
                if state:
                    return True
    # if [co[0]][co[1]] != '#' or [co[0]][co[1]] != 'o':
    tetris[co_ordinates[0]][co_ordinates[1]] = 'o'
    return False
counter = 0
co_ordinates = [sand_poring[1]+1,sand_poring[0]-mega]
r_settle(tetris,co_ordinates,counter)
#%% Part 2
tetris = [['.'] * 500 for i in range(0,200)]
# tetris[16][47] = '#'
for i in mapper:
    tetris[i[1]][i[0]] = '#'
    max_rock_depth = max(max_rock_depth,i[1])
tetris[sand_poring[1]][sand_poring[0]-mega] = '+'
moves = [(0,1),(0,-1),(1,0),(-1,0)]
counter = 0
for idx,i in enumerate(tetris[max_rock_depth+ 2]):
    tetris[max_rock_depth+ 2][idx] = '#'

def r_settle(tetris,co_ordinates,counter=0):
    print(max_rock_depth,co_ordinates[1])
    mvs = [(1,0),(1,-1),(1,1)]
    for i in mvs:
        co = [co_ordinates[0]+i[0],co_ordinates[1]+i[1]]
        if co[1] >= 0 or co[1] < len(tetris[0]) or co[0] >= 0 or co[0] < len(tetris):
            if tetris[co[0]][co[1]] == '.' or tetris[co[0]][co[1]] == '+': 
                counter +=1
                r_settle(tetris,co,counter)
    tetris[co_ordinates[0]][co_ordinates[1]] = 'o'
    return False
counter = 0
co_ordinates = [sand_poring[1],sand_poring[0]-mega]
r_settle(tetris,co_ordinates,counter)
#%%
counter = 0
for i in tetris:
    for j in i:
        if j == 'o':
            counter +=1
counter
# %%
for i in tetris:
    print(''.join(i))


# %%
