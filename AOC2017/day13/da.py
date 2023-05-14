#%%
from collections import defaultdict
counter  = 0
d = defaultdict(int)
max_v = 0
for i in open('input.txt').read().splitlines():
    d[int(i.split(': ')[0])] = int(i.split(': ')[1])

max_v = max(d.keys())

# %%
import math
def okay_to_pass(i):
    # print(i,d[i],i%d[i],math.ceil(i / (d[i]))%2)
    print(i)
    if i in d:
        if  i / (d[i]-1) % 2 == 0:
            return False
        return True
    return True
vals = []
for i in range(0, max_v+1):
    if i in d:
        if not okay_to_pass(i):
            print('caught', f'{i} % {(d[i])} = {i % (d[i])}' ,d[i]*i,math.ceil(i / (d[i]-1)) % 2,)
            vals.append(i*d[i])
sum(vals)
# %%
def okay_to_pass1(val,i):
    if i in d:
        if  (val + i) / (d[i]-1) % 2 == 0:
            return False
        return True
    return True
# %% Brute force part2
for i in range(0,10000000):
    vals = []
    delay = i 
    for i in range(0, max_v+1):
        if i in d:
            if not okay_to_pass1(delay,i):
                vals.append('9')
                break
    if vals == []:
        print('delay',delay)
        break

# %%
in_order = [0
,2
,3
,4
,5
,6
,7
,8
,9]
# %%
for idx,i in enumerate(in_order):
    if i in (2,8):
        print(idx,i)
    
# %%
in_order[1:8]
# %%
