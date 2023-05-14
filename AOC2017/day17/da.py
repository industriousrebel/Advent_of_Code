#%%
puzzle_input = 344
# puzzle_input = 3
# %%
from collections import defaultdict

def part_1(puzzle_input):
    arr = []
    val = 0
    size = 1
    idx = 0
    steps = puzzle_input
    for i in range(2018):
        if val == 2017:
            temp = idx
        arr = arr[:idx] + [val] + arr[idx:]
        # print(arr)
        idx = ((idx + steps) % size) + 1
        val +=1
        size += 1
    print(arr[temp:temp+2][-1])
# %%
def part_2(puzzle_input):
    val = 0
    size = 1
    idx = 0
    steps = puzzle_input
    hm = defaultdict(int)
    for i in range(50000000):
        idx = ((idx + steps) % size) + 1
        val +=1
        size += 1
        if idx == 1:
            hm[idx]= val
    print(hm[1])

# %%
part_1(puzzle_input)
# %%
part_2(puzzle_input)

# %%
