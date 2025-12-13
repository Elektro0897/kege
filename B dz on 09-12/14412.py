from itertools import *
k = 0
for val in product('алгоритм', repeat=6):
    val = ''.join(val)
    val = val.replace('о', '*')
    val = val.replace('и', '*')
    val = val.replace('а', '*')
    if val.count('л') <= 1 and val[0] != 'р' and val[-1] == '*':
        k += 1
print(k)