from itertools import *
from string import printable as alf
k = 0
for val in product(alf[:14], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if val[-1] in '03' and len(set(val)) == 2:
            k += 1
print(k)