from itertools import *
s = sorted('парус')
for pos, val in enumerate(product(s, repeat=5), start=1):
    val = ''.join(val)
    if 'аа' not in val and val.count('у') <= 0:
        print(pos)
        break
        #131