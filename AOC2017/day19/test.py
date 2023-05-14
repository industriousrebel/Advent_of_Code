#%%
input = [list(i.replace('\n','')) for i in open('./input.txt').readlines()]
moves = [(0,1),(1,0),(0,-1),(-1,0)]
def direction(pos_y,pos_x,moves,prev):
    for my,mx in moves:
            n_y = pos_y+my
            n_x = pos_x+mx
            if n_y > 0 and n_y < len(input) and n_x > 0 and n_x < len(input[0]):
                if input[n_y][n_x] != ' ' and (n_y,n_x) not in prev:
                    # print(my,mx)
                    return (my,mx)
ret_stack = []

for idx,i in enumerate(input[0]):
    if i != ' ':
        pos_x = idx
pos_y = 0
prev = set()
m = direction(pos_y,pos_x,moves,prev)
counter = 1
# print(counter,input[pos_y][pos_x])
while m != None:
        m = direction(pos_y,pos_x,moves,prev)
        if m == None or m == ' ':
            break
        pos_y += m[0]
        pos_x += m[1]
        prev.add((pos_y,pos_x))
        counter +=1
        # print(counter,input[pos_y][pos_x])
        while input[pos_y][pos_x] != '+':
            if input[pos_y][pos_x] not in ('-','|','+', ' '):
                ret_stack.append(input[pos_y][pos_x])
            pos_y += m[0]
            pos_x += m[1]
            if input[pos_y][pos_x] == ' ':
                break
            prev.add((pos_y,pos_x))
            counter+=1
            # print(counter,input[pos_y][pos_x],m)
# %%
print(''.join(ret_stack),counter)


# %%
