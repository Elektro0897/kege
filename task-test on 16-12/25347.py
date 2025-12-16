from itertools import *
alf = sorted('гранит')
k = 0
for pos, val in enumerate(product(alf, repeat=6), start=1):
    val = ''.join(val)
    if val[0] not in 'аиг' and val.count('а') == 1 and pos % 2 != 0:
        print(pos)
        break
