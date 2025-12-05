from itertools import *
k = 0
for val in product('гепард', repeat=5):
    val = ''.join(val)
    if val.count('г') == 1 and val[0] != 'а' and val[-1] != 'е':
        k += 1
print(k)