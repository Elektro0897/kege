from itertools import *
k = 0
alf = sorted('парус')
for pos, val in enumerate(product(alf, repeat=5), start=1):
    val = ''.join(val)
    if not (val[0] == 'у' and 'аа' not in val):
        k += 1
    else:
        print(k+1)
        break
print('ответ: 2527')
