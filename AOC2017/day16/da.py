#%%
def spin(arr, size):
    return arr[-size:] + arr[:-size]
def exchange(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr
def partner(arr, a, b):
    return exchange(arr, arr.index(a), arr.index(b))
# %%
def dance(arr, moves):
    for move in moves:
        if move[0] == 's':
            arr = spin(arr, int(move[1:]))
        elif move[0] == 'x':
            a, b = move[1:].split('/')
            arr = exchange(arr, int(a), int(b))
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            arr = partner(arr, a, b)
    return arr
# %
#%%
input1 = list('abcdefghijklmnop')
input2 = open('input.txt').read().strip()
# input1 = list('abcde')
# input2 = 's1,x3/4,pe/b'
input2 = input2.split(',')
e = set()
s = {}
counter = 0
while True:
    x = ''.join(input1)
    s[counter] = x
    if x in e:
        cycle = counter
        break
    input1 = dance(input1, input2)
    e.add(x)

    counter += 1
cyclic_idx =  1000000000 % cycle
print(s[1],s[cyclic_idx])
# %%
is_palindrome('abba')
# %%
def is_palindrome(s):
    return s == s[::-1]