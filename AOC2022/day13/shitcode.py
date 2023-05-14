        # ret = []
        # stack = []
        # p = ret
        # for c in parse_str[1:-1]:
        #     # print(c)
        #     if c == '[':
        #         stack.append(p)
        #         p.append([])
        #         p = p[-1]
        #     elif c == ']':
        #         p = stack.pop()
        #     elif c != ',':
        #         p.append(int(c))
        # nd.append(ret)\
    # for n_idx,k in enumerate(t_l):
    #     if k[0] < t_r[n_idx][0] and k[1] == t_r[n_idx][1]:
    #         print(i)
            # ans.append(idx)
    # print(t_l,t_r)
ans
# %%
print(ho[0])
# %%
t_l
# %%

l = recursive_arr(a,[],0)
r = recursive_arr(b,[],0)

# %%
[]
# %%
# %%
# def recur_arr(value,count=0):
#     if value == []:
#         return (-1,count+1)
#     if type(value) == list:
#         return recur_arr(value[0],count+1)
#     if type(value) == int:
#         return (value,count)   
        
# def recursive_arr(arr,lst=[]):
#     for i in arr:
#         if type(i) == list:
#             # lst.append(i)
#             recursive_arr(i,lst)
#         else:
#             lst.append(i)
#             # print(i,)
#     return lst
# ho = s.copy()
# ans = []
# for idx,i in enumerate(ho):
#     print(i[0],i[1])
#     # if len(i[0]) <= len(i[1]):
#     t_l = recursive_arr(i[0])
#     t_r = recursive_arr(i[1])
#     print(t_l,t_r)
#         # for idx,i in enumerate(t_l):
        #     print(i,t_r[idx])
        #     if i < t_r[idx]:
        #         print(i)
        #         ans.append(idx)
        #         break


            # if  < :
            #     ans.append(idx)
            #     break
# stack = []
# def recursive_arr(arr,lst=[],depth=0,stack=[]):
#     for a in arr:
#         # if a == []:
#         #     lst.append([])
#         if type(a) == list:
#             # lst.append(i)
#             recursive_arr(a,lst,depth)
#         else:
#             lst.append(a)
#             # print(i,)
#     return lst

# def new_recurr(arr):
#     hm = defaultdict(list)
#     for i in arr:
#         hm[i[1]].append(i[0])
#     return hm