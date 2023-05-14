#%%
data = [ i.replace('\n', '').split(' ') for i in open('day10.txt').readlines()]
reg = 1
# %%
for idx,i in enumerate(data[:20]):
    if i[0] == 'noop':
        print('noop', idx)
# %%
