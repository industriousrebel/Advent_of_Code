#%%
from collections import defaultdict
from functools import reduce
class Node():
  def __init__(self,name,val = 0,parent = None,folder=False):
    self.val = val
    self.name = name
    self.folder = folder
    self.parent = parent
    self.children = []

commands = [i.replace('\n','') for i in open('input.txt').readlines()]
s = Node(None)
s.children = [Node(val = 0,name = '/',parent = s)]
curr = s
for tdx,i in enumerate(commands):
  if '$ cd' in i:
    if '$ cd ..' in i:
      curr = curr.parent
    else:
      for child in curr.children:
        if child.name == i.split(' ')[-1]:
          curr = child
    idx = tdx+1
    while idx < len(commands) and '$ cd' not in commands[idx]:
      if 'dir ' in commands[idx]:
        curr.children.append(Node(name = commands[idx].split(' ')[-1],val = 0,parent = curr,folder=True))
      elif '$ ls' not in commands[idx]:
        curr.children.append(Node(val = int(commands[idx].split(' ')[0]),name = commands[idx].split(' ')[1],parent = curr))
      idx +=1

#%%
p = s.children[0]
def recursive_sum(p):
    if p.children == []:
        return 0
    else:
        # for x in p.children:
        #     return x.val + recursive_sum(x)
        return sum([x.val + recursive_sum(x) for x in p.children])
        # return reduce(lambda x,y: x+y,map(lambda x: x.val + recursive_sum(x),p.children))
#%%
max_summers = []
stack = [p]
dir_sizes = []
while stack:
    curr = stack.pop()
    # if curr.name == 'hvfvt':
    #     for i in curr.children:
    #         print(i.val,i.name)
    ret = recursive_sum(curr)
    if  ret != 0 and ret <= 100000:
        max_summers.append(ret)
    if  ret != 0:
        dir_sizes.append((curr.name,ret))
    for i in curr.children:
        stack.append(i)
    
# %%
dir_sizes
# %%
sum(max_summers)
# %%
outer_most_dir = recursive_sum(p)
outer_most_dir
# %%
space_needed = 30000000 - (70000000 - outer_most_dir)
space_needed
# %%
dir_sizes = sorted(dir_sizes,key=lambda x: x[1],reverse=True)
dir_sizes[:10]
# %%
s = outer_most_dir
for i in dir_sizes:
    if i[1] >= space_needed:
        s = min(s,i[1])
# %%
for d in dir_sizes:
    if d[0] == 'hvfvt':
        print(d[1])
    if d[1] == s:
        print(d[0],d[1])
# %%
# %%


# %%
