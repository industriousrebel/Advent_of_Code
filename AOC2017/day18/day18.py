#%%
input = [i.replace('\n','').split(' ') for i in open('input.txt').readlines()]
# %%
from collections import defaultdict
sound = None
registers = defaultdict(int)

indx = 0
while indx < len(input):
    i = input[indx]
    print(indx,i,registers)
    if i[0] == 'set':
        if i[2] in registers: 
            registers[i[1]] = int(registers[i[2]])
        else:
            registers[i[1]] = int(i[2])
    elif i[0] == 'add':
        if i[2] in registers: 
            registers[i[1]] += int(registers[i[2]])
        else:
            registers[i[1]] += int(i[2])
    elif i[0] == 'mul':
        if i[2] in registers: 
            registers[i[1]] *= int(registers[i[2]])
        else:
            registers[i[1]] *= int(i[2])
    elif i[0] == 'mod':
        if i[2] in registers: 
            registers[i[1]] %= int(registers[i[2]])
        else:
            registers[i[1]] %= int(i[2])
    elif i[0] == 'snd':
        sound = registers[i[1]]
    elif i[0] == 'rcv':
        if registers[i[1]] != 0:
            print(sound)
            break
    elif i[0] == 'jgz':
        if registers[i[1]] > 0:
            indx += int(i[2]) - 1
    indx += 1
# %%
4 += -2 = 2 - 1 + 1 = 2
4 += 2 = 6 - 1 = 5