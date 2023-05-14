#%%
from collections import deque
test_input = open('input.txt').read().strip()
states = deque(['normal'])
groups = 0
garbage = 0
idx = 0
while idx < len(test_input):
    layer = states.count('normal')
    char = test_input[idx]
    state = states[-1]
    if state == 'normal':
        if char == '{':
            groups += 1*layer
            states.append('normal')
        elif char == '}':
            states.pop()
        elif char == '<':
            states.append('garbage')
    elif state == 'garbage':
        if char == '>':
            states.pop()
        elif char == '!':
            idx += 1
        else:
            garbage += 1
    idx += 1
print(f'Part1 {groups}, Part 2 {garbage}')
# %%
