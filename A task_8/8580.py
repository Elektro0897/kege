from itertools import *
from string import *
p = printable[:13]
k = 0
for val in product(p, repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val.count('0') >= 2:
        for i in printable[10:13]:
            val = val.replace(i, '*')
        if '**' in val and val.count('*') == 2:
            k += 1
print(k)
#13779