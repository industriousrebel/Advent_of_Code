#%%
data = [i.strip() for i in open('input.txt').readlines()]
class Node:
    def __init__(self,name,weight,children=[],parent=None):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = None
        self.balanced_weight = 0
# %%
from collections import defaultdict,deque,Counter
d = defaultdict(list)
for i in data:
    name = i.split(' ')[0]
    weight = int(i.split(' ')[1].strip('()'))
    if '->' in i:
        children = [j.strip(',') for j in i.split('->')[1].split()]
        d[name] = [weight,children]  
    else:
        d[name] = [weight,[]]
for i in d:
    curr_node = Node(name = i,weight = d[i][0],children = [],parent = None)
    d[i].append(curr_node) 
for i in d:
    if d[i][1] != []: 
        for child in d[i][1]:
            d[i][2].children.append(d[child][2])
            d[child][2].parent = d[i][2]

for i in d:
    random_node = d[i][2]
    break
while random_node.parent != None:
    random_node = random_node.parent
    print(random_node.children) 
print(random_node.name)
# %%
top_node = random_node
# %%
ret_ret = []
def dfs(node):
    # print(node.name)
    if node is None: return 0
    s = node.weight
    ls = []
    for c_node in node.children:
        sk = dfs(c_node)
        ls.append(sk)
        s +=  sk
    # print(ls)
    mx = Counter(ls)
    
    if len(mx) > 1:
        vall = mx.most_common(1)[0][0]
        print(node.name,ls)
        for i in node.children:
            if i.balanced_weight != vall:
                print(i.name,i.balanced_weight,i.weight)
                ret_ret.append(i.weight - (i.balanced_weight - vall))
            # for k in i.children:
            #     print(k.balanced_weight)

    node.balanced_weight = s
    return node.balanced_weight
it_node = top_node
dfs(it_node)
print(ret_ret[0])


# %%

# %%
