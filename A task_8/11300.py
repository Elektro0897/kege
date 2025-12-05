from itertools import *
alf = sorted('гондбуш')
for pos, val in enumerate(product(alf, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'б' and val.count('н') >= 2 and val.count('у') == 0 and pos % 2 != 0:
        pos1 = pos
print(pos1)