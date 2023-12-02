#%%
from functools import reduce
from operator import mul,add
games = [i.split(': ')[-1].replace('\n','').split(';') for i in open('input.txt').readlines()]
ids = [int(i.split(': ')[0].replace('Game ','')) for i in open('input.txt').readlines()]
counter = 0
stack = []
for idx,game in enumerate(games):
    valid = True
    cube_set = {'red': 0 ,'green':0, 'blue': 0}
    for show in game:
        cubes = {'red': 12, 'green':13, 'blue':14}
        f = [i.split(' ')[-2:] for i in show.split(',')]
        for val,color in f:
            cube_set[color] = max(cube_set[color],int(val))
            cubes[color] -= int(val)
        if min(cubes.values()) < 0:
            valid = False
    stack.append(list(cube_set.values()))
    if valid:
        counter += ids[idx]
print(counter)
print(reduce(add,[reduce(mul,i) for i in stack]))

# %%

# %%
