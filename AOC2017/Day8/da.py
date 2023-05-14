import operator
max_val = 0
op_map = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    'inc': operator.add,
    'dec': operator.sub
}
#%%
hm = {}
for i in data:
    if op_map[i[5]](hm[i[4]],int(i[6])):
        val = op_map[i[1]](hm[i[0]],int(i[2]))
        max_val = max(op_map[i[1]](hm[i[0]],int(i[2])),hm[i[0]],max_val)
        hm[i[0]] = val