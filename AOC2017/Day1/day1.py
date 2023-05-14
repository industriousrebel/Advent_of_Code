#%%
test = open('input.txt').read()
vals = 0
for p in range(0,len(test)):
    if test[p] == test[(p + (len(test) // 2)) % len(test)]:
        vals += int(test[p])
# %%
vals
# %%
