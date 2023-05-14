#%%
from collections import defaultdict
from json import loads
data =  [i.replace('\n','') for i in  open('test.txt').readlines() ]
# %%
s = []
nd = []
for parse_str in data:
    if parse_str == '':
        s.append(nd)
        nd = []
    else:
        nd.append(loads(parse_str))


# %%
ho = s.copy()
# %%

def compare(l,r):
    # print(l,r)
    if type(l) == list and type(r) == int:
        return compare(l,[r])
    elif type(r) == list and type(l) == int:
        return compare([l],r)
    elif type(l) == int and type(r) == int:
        if l < r:
            return True
        if r < l:
            return False
    elif type(l) == list and type(r) == list:
        l_idx = 0
        r_idx = 0
        while l_idx < max(len(l),len(r)):
            sl = l[l_idx] if l_idx < len(l) else None
            sr = r[r_idx] if r_idx < len(r) else None
            if sl == None and sr != None:
                return True
                break
            ret = compare(sl,sr)
            if ret != None:
                return ret
            if l_idx < len(l):
                l_idx +=1
            if r_idx < len(r):
                r_idx +=1   
    else:
        return False
        

# %%
ans = set()
for idx, i in enumerate(ho[:]):
    is_good = compare(i[0],i[1])
    if is_good == True:
        ans.add(idx+1)
    # break
# %%
sum(ans)
# %%
ho =  [loads(i.replace('\n','')) for i in  open('Input.txt').readlines() if i.replace('\n','') != '']
ho.append([[2]])
ho.append([[6]])
# %%
new_ho = []
for h in ho:
    new_ho.append(h)
# %%
def new_compare(a,b):
    if compare(a,b) == True:
        return 1
    else:
        return -1
# sorted(ho,key=compare)
from functools import cmp_to_key
new = sorted(new_ho, key=cmp_to_key(new_compare),reverse=True)
new
#%%
ret = []
for idx,i in enumerate(new):
    if i in ([[[2]],[[6]]]):
        ret.append(idx+1)

print(ret[0]*ret[1])
# %%
