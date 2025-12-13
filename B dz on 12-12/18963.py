from itertools import *
k = 0
for val in product('котбус', repeat=8):
    val = ''.join(val)
    if val.count('кот') >= 1 and val[0] not in 'оу':
        k += 1
print(k)