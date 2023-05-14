#%%


#%%
"""
1. Take the previous value.
2. Multiply it by a factor (generator_a = 16807, generator_b = 48271)
3. Divide the result by 2147483647
"""


# %%
generator_a = 618
generator_b = 814
# generator_a = 65
# generator_b = 8921

from functools import reduce
gen_a = []
gen_b = []
counter = 0
for i in range(0,50000000): #
    if len(gen_a) >= 5000000 and len(gen_b) >= 5000000:
        break
    # if i%1000000 == 0:
    #     print(i / 40000000)
    generator_a = (generator_a*16807) % 2147483647
    generator_b = (generator_b*48271) % 2147483647
    if generator_a % 4 == 0:
        gen_a.append(bin(generator_a)[-16:])
    if generator_b % 8 == 0:
        gen_b.append(bin(generator_b)[-16:])
    counter +=1 if bin(generator_a)[-16:] == bin(generator_b)[-16:] else 0
# %%
counter = 0
for i in range(0,min(len(gen_a),len(gen_b))):
    if gen_a[i] == gen_b[i]:
        counter += 1
# %%
counter
# %%
min(len(gen_a),len(gen_b))
# %%
