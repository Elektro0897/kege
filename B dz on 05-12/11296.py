from itertools import *
alf = sorted('досж')
for pos, val in enumerate(product(alf, repeat=6), start=1):
    val = ''.join(val)
    if val[:2] == 'жс':
        print(pos)
        break
print('ответ: 1793')