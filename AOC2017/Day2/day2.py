#%%
file =  [list(map(int,i.replace('\n','').split('')))for i in open("input.txt").readlines()]
# %%
ret = 0
for i in file:
    ret += max(i) - min(i)
# %%
#%% part2
file =  [list(map(int,isplit('\t')))for i in open("input.txt").readlines()]
# %%
ret = 0
for i in file:
    for vdx,v in enumerate(i):
        for sdx,s in enumerate(i):
            # print(i)
            if sdx != vdx and v % s == 0:
                # print(v,s,v//s)
                ret += v // s
# %%
