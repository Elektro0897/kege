from itertools import *
k = ''
alf = sorted('гирлянда')
for pos, val in enumerate(product(alf, repeat=6), start=1):
    val = ''.join(val)
    if val[:1] != 'я' and val.count('д') == 3 and pos % 2 == 0:
        k = pos
print(k)
print('ответ: 226456')