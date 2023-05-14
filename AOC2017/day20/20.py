#%%
import re
input = [i.replace('\n','') for i in open('input.txt').readlines()]
#%%

# %%
def part1():
    d = {}
    for idx,i in enumerate(input):
        p,v,a = i.split(', ')
        p = list(map(int,re.sub('[^0-9,-]','',p).split(',')))
        v = list(map(int,re.sub('[^0-9,-]','',v).split(',')))
        a = list(map(int,re.sub('[^0-9,-]','',a).split(',')))
        d[idx] = {'pos':p,'vel':v,'acc':a}
    for count in range(1000):
        for k in d.keys():
            d[k]['vel'] = [d[k]['vel'][i]+d[k]['acc'][i] for i in range(3)]
            d[k]['pos'] = [d[k]['pos'][i]+d[k]['vel'][i] for i in range(3)]
        def md(x,y,z):
            return abs(x)+abs(y)+abs(z)
        min_k = 0
        min_d = md(d[0]['pos'][0],d[0]['pos'][1],d[0]['pos'][2])
        for k in d.keys():
            if md(d[k]['pos'][0],d[k]['pos'][1],d[k]['pos'][2]) < min_d:
                min_d = md(d[k]['pos'][0],d[k]['pos'][1],d[k]['pos'][2])
                min_k = k
        print(min_k)
# %%
from collections import defaultdict
def part2():
    d = {}
    for idx,i in enumerate(input):
        p,v,a = i.split(', ')
        p = list(map(int,re.sub('[^0-9,-]','',p).split(',')))
        v = list(map(int,re.sub('[^0-9,-]','',v).split(',')))
        a = list(map(int,re.sub('[^0-9,-]','',a).split(',')))
        d[idx] = {'pos':p,'vel':v,'acc':a}
    for count in range(10000):
        collisions = defaultdict(list)
        for k in d.keys():
            d[k]['vel'] = [d[k]['vel'][i]+d[k]['acc'][i] for i in range(3)]
            d[k]['pos'] = [d[k]['pos'][i]+d[k]['vel'][i] for i in range(3)]
            curr_pos = ''.join(map(str,d[k]['pos']))
            # print(curr_pos)
            collisions[curr_pos].append(k)
        for k in collisions.keys():
            if len(collisions[k]) > 1:
                for i in collisions[k]:
                    del d[i]
    print(len(d))
            
  
# %%
part2()
# %%

# %%
