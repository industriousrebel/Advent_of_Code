#%%
from collections import defaultdict
input =  open('input.txt').readline().strip().split(',')
d = defaultdict(int)
max_dist = 0 
for i in input:
    d[i] += 1
    s  = d['s'] - d['n'] + ((d['sw'] - d['se'] ) - (d['ne'] - d['nw']))
    south1 = d['s'] - d['n']
    southwest = d['sw'] - d['ne']
    northwest = d['nw'] - d['se']
    dist = south1 + min(southwest,northwest) + (southwest - northwest)
    max_dist = max(max_dist,dist)

max_dist
# %%
# %%
south1 + min(southwest,northwest) + (southwest - northwest)
# %%
# %%
input
# %%
d = [0,0,0,0,0,0]

for i in input:
    d[]
    if i == 'n':
        d
    south1 = d['s'] - d['n']
    southwest = d['sw'] 
    northwest = d['nw']
    dist = south1 + min(southwest,northwest) + (southwest - northwest)
    max_dist = max(max_dist,dist)

# %%
max_dist
# %%
