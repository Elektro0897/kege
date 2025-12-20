from itertools import *
k = 0
alf = sorted('престол')
for pos, val in enumerate(product(alf, repeat=5), start=1):
    val = ''.join(val)
    for i in val:
        if i in 'ео':
            val = val.replace(i, '-')
        else:
            val = val.replace(i, '=')
    if val[-1] == '-' and val.count('=') <= 3 and pos % 2 != 0:
        k += 1
print(k)
# ответ 1776