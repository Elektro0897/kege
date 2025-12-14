from itertools import *
k = 0
alf = sorted('сентябрь')
for pos, val in enumerate(product(alf, repeat=5), start=1):
    val = ''.join(val)
    if val[0] == 'р' and val.count('ь') == 0 and pos % 2 == 0:
        k = pos
print(k)