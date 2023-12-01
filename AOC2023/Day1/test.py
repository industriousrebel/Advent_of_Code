#%%
si = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
nums = [i.replace('\n','') for i in open('input.txt').readlines()]

# %%
output = 0
for i in nums:
    stack = []
    for num in i:
        if num.isnumeric():
            stack.append(num)
    output += int(stack[0] + stack[-1])
    print(stack,output)
print(output)

# %%
output = 0
size_list = (3,4,5)
for sdx,i in enumerate(nums):
    stack = []
    size = len(i)
    for idx,num in enumerate(i):
        if num.isnumeric():
            stack.append(num)
        else:
            for x in size_list:
                if idx+x <= size:
                    if i[idx:idx+x] in si:
                        stack.append(si[i[idx:idx+x]])
    val = int(str(stack[0]) + str(stack[-1]))
    output += val
output
# %%
