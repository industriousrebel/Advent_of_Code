#%%
import operator
from functools import reduce
from math import gcd,lcm

ops = {     
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor}
data  = [i.replace('\n', '') for i in open('input.txt').readlines()]
from math import log2
 
# %%
i = 0
new_arr = []
m = {}
while i < len(data):
    if 'Monkey' in data[i]:
        monkey_num = data[i].split(' ')[-1][:-1]
        m[monkey_num] = {}
        m[monkey_num]['Inspection'] = 0
    if 'Starting items' in data[i]:
        m[monkey_num]['Starting items'] = [int(i) for i in data[i].split(':')[-1].split(', ')]
    if 'Operation' in data[i]:
        m[monkey_num]['operations'] = [ops[data[i].split('=')[-1].strip().split(' ')[1]],data[i].split('=')[-1].strip().split(' ')[0],data[i].split('=')[-1].strip().split(' ')[-1]]
        # m[monkey_num]['operationoutput'] = l
    if 'Test'  in data[i]:
        m[monkey_num]['test'] = int(data[i].split('by')[-1].strip())
    if 'true' in data[i]:
        m[monkey_num]['True'] = data[i].split(' ')[-1] 
    if 'false' in data[i]:
        m[monkey_num]['False'] = data[i].split(' ')[-1]
        # new_arr.append(m)
    i+=1

for _ in range(10001):
    total = []
    # print(f'Round {_}')
    if _ in (0,1,20,100,1000,2000,3000,4000,5000,10000,10001):
        for kma in m.values():
            total.append(kma['Inspection'])
        r = reduce((lambda x, y: x * y), list(sorted(total)[-2:]))
        # print('---------------')
        print(_,total,r)
        # print('---------------')

    i = 0
    while i < len(m):
        # print('Round',_,'Monkey',i)
        monkey_num = str(i)
        #  len(m[monkey_num]['Starting items'])
        for idx,element in enumerate(m[monkey_num]['Starting items']):
            m[monkey_num]['Inspection'] += 1
            #Calculate new value / test  == int
            d = m[monkey_num]['operations']
            x = element if d[1] == 'old' else int(d[1])
            y = element if d[-1] == 'old' else int(d[-1])
            mod = lcm(*[i['test'] for i in m.values()])
            new_value = d[0](x% mod, y% mod) % mod #d[0](x, y)
            # if new_value % m[monkey_num]['test'] != temp % m[monkey_num]['test']:
            # print(element,new_value,m[monkey_num]['test'], new_value % m[monkey_num]['test'])
            if new_value % m[monkey_num]['test']  == 0:
                m[m[monkey_num]['True']]['Starting items'].append(new_value)
            else:
                m[m[monkey_num]['False']]['Starting items'].append(new_value)
        m[monkey_num]['Starting items'] = []
            # print(m)


        i+=1

total = []
for i in m.values():
    total.append(i['Inspection'])



#%%
lcmm = 
# %%

# %%
lcmm
# %%
