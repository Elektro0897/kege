from itertools import *
k = 0
alf = sorted('гирлянда')
for pos, val in enumerate(product(alf, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'я' and val.count('д') == 3 and pos % 2 == 0:
        k += 1
print(k)
print('ответ: 1848')