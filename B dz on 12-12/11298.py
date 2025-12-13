from itertools import *
k = 0
alf = sorted('жопаюз')
for pos, val in enumerate(product(alf, repeat=6),start=1):
    val = ''.join(val)
    if val[0] == 'а' and val.count('з') >= 2 and pos % 2 == 0:
        k += 1
print(k)