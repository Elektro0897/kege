from itertools import *
s = sorted('школа')
for pos, val in enumerate(product(s, repeat=5), start=1):
    val = ''.join(val)
    if 'шалаш' in val:
        print(pos)