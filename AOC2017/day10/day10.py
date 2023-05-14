#%%

inp = [i for i in range(256)]
# inp = [i for i in range(5)]
lens = [189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62]
# lens = [3, 4, 1, 5]
def knot_algo(inp,lens):
    idx = 0
    start = 0
    skip_size = 0
    while idx < len(lens):
        curr_len = lens[idx]
        end_idx = (start+curr_len) 
        if end_idx > len(inp):
            slice = inp[start:] + inp[:end_idx % len(inp)]
            slice_idx = [x for x in range(start, len(inp))] + [x for x in range(0, end_idx % len(inp))]
        else:
            slice = inp[start: end_idx]
            slice_idx = [x for x in range(start, end_idx)]
        # print(start,end_idx,lens[idx],slice,slice_idx,skip_size)
        for sdx,iddi in enumerate(reversed(slice)):
            inp[slice_idx[sdx]] = iddi
        # print(inp)
        start = (start + curr_len + skip_size) % len(inp)
        skip_size += 1
        idx += 1
    return inp
# %%
inp = knot_algo(inp,lens)
print(inp[0] * inp[1])
# %% Part 2
def knot_algo2(start,skip_size,inp,lens):
    idx = 0
    while idx < len(lens):
        curr_len = lens[idx]
        end_idx = (start+curr_len) 
        if end_idx > len(inp):
            slice = inp[start:] + inp[:end_idx % len(inp)]
            slice_idx = [x for x in range(start, len(inp))] + [x for x in range(0, end_idx % len(inp))]
        else:
            slice = inp[start: end_idx]
            slice_idx = [x for x in range(start, end_idx)]
        # print(start,end_idx,lens[idx],slice,slice_idx,skip_size)
        for sdx,iddi in enumerate(reversed(slice)):
            inp[slice_idx[sdx]] = iddi
        # print(inp)
        start = (start + curr_len + skip_size) % len(inp)
        skip_size += 1
        idx += 1
    return inp,start,skip_size
# %%

data = '189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62'
def return_hash(data):
    inp = [i for i in range(256)]
    nl = [ord(i) for i in data] + [17, 31, 73, 47, 23]
    start = 0
    skip_size = 0
    for i in range(64):
        inp,start,skip_size = knot_algo2(start,skip_size,inp,nl)
    # inp = [ord(i) for i in 'AoC 2017'] + [17, 31, 73, 47, 23]
    hash = []

    for x in range(len(inp)//16):
        hash.append(inp[16*x])
        for y in range(1,16):
            # print(hash[x],inp[16*x+y],hash[x] ^ inp[16*x+y])
            hash[x] = hash[x] ^ inp[16*x+y]
    for idx,k in enumerate(hash):
        if len(hex(k)[2:]) == 1:
            hash[idx] = '0' + hex(k)[2:]
        else:
            hash[idx] = hex(k)[2:]
        
    hexxx = ''.join(hash)
    # print(hexxx)
    return hexxx

# %%
# %%
