#%%
test = [int(k) for k in [i.strip().split() for i in open('input.txt').readlines()][0]]
# test = [0,2,7,0]
seen = set()
counter = 0
while tuple(test) not in seen:
    counter += 1
    seen.add(tuple(test))
    max_index,max_val = max(enumerate(test),key=lambda x: x[1])
    test[max_index] = 0
    for i in range(max_val):
        test[(max_index + i + 1) % len(test)] += 1

seen2 = set()
print(seen2)
counter = 0
while tuple(test) not in seen2:
    counter +=1
    seen2.add(tuple(test))
    max_index,max_val = max(enumerate(test),key=lambda x: x[1])
    test[max_index] = 0
    for i in range(max_val):
        test[(max_index + i + 1) % len(test)] += 1
# %%
counter
# %%
