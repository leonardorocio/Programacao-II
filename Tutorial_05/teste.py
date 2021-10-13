d = 89
lst = []
# for i, v in enumerate(rng):
#     if i % 2 == 0:
#         d += (30 + i)
#     else:
#         d -= (23 + i)
#     lst.append(d)

# print(lst[:10]) 

i = 0
v = 0
c = 0
while d < 1501 and c < 1000:
    if c % 2 == 0:
        d += (30 + i)
        i += 1
    else:
        d -= (23 + v)
        v += 1
    c += 1
    lst.append(d)
# print(lst)
print(lst.index(999))
nl = lst[220:]
result = sum(1 for i in nl if i >= 1000)
print(result)