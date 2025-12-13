from itertools import *
k = 0
alf = sorted('сублимаця')
for pos, val in  enumerate(product(alf, repeat=5), start=1):
    val = ''.join(val)
    val = val.replace('у', '*')
    val = val.replace('и', '*')
    val = val.replace('а', '*')
    val = val.replace('я', '*')
    if val.count('*') == 2 and val[-1] != 'я' and pos % 2 != 0:
        k = pos
print(k)