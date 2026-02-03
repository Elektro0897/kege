from string import printable as alf
from itertools import *
k = 0
l = 0
s = sorted('крате')
for pos, val in enumerate(product(s, repeat=6), start=1):
    val = ''.join(val)
    if val in 'карета':
        k = pos
    if val in 'ракета':
        l = pos
print(l - k - 1)
# ответ: 2999