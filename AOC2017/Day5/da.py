#%%
data = [int(i.strip()) for i in open('input.txt').readlines()]
# %%
# data = [0,3,0,1,-3]
# i = 0
# counter = 0
# current = 0
# jump = 0
# while i < len(data):
#     # print(data)
#     jump += data[i]
#     data[i] += 1
#     i = jump
#     if jump > len(data) or i > len(data):
#         break
#     counter +=1

# %% Part2
data = [int(i.strip()) for i in open('input.txt').readlines()]

i = 0
counter = 0
jump = 0
while i < len(data):
    # print(data)
    jump += data[i]
    if data[i] >= 3:
        data[i] -= 1
    else:
        data[i] += 1
    i = jump
    counter +=1
counter
# %%
len(data)
# %%
