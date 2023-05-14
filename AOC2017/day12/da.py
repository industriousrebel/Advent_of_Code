#%%
from collections import defaultdict
f = [[i.split(' <-> ')[0],i.split(' <-> ')[1].split(', ')]
 for i in open('input.txt').read().splitlines()]
# %%
d = defaultdict(set)
for i in f:
    for k in i[1]:
        d[i[0]].add(k)

# %% Part 2.
visited = set()
stack = []
group_counter = 0
for i in d:
    if i not in visited:
        stack.append(i)
        group_counter += 1
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(d[node])
# %%
group_counter
# %%
d
# %%
