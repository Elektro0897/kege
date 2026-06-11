from itertools import *
s = sorted('поленица')
for pos, val in enumerate(product(s, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] != 'а' and val[-1] != 'а' and val.count('л') >= 3:
        print(pos)
        break
        #5851