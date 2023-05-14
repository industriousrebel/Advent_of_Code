#%%
file = [ i.strip().split(' ') for i in open("input.txt").readlines()]
counter = 0
for x in file:
    s = set()
    for y in x:
        s.add()
    if len(s) == len(x):
        counter += 1
# %%
from functools import reduce
import operator
reduce(operator.add,[len(set([''.join(sorted(y)) for y in x])) == len(x) for x in file])

# %%
# %%
