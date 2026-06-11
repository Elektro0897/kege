from itertools import *
from string import *
p = printable[:5]
k = 0
for val in product(p, repeat=9):
    val = ''.join(val)
    if val[0] != '0':
        for i in printable[:5:2]:
            val = val.replace(i, '*')
        if val.count('**') == 2 and '***' not in val:
            k += 1
print(k)
#151200