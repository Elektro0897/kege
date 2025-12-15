from itertools import *
k = 0
alf = sorted('бмюрн')
for pos, val in enumerate(product(alf, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'м' and val.count('р') >= 2 and val.count('ю') == 0 and pos % 2 != 0:
        k = pos
print(k)