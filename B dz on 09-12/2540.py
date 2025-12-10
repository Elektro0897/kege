from itertools import *
k = 0
alf = sorted('автор')
for pos, val in enumerate(product(alf, repeat=4), start=1):
    val = ''.join(val)
    if val != 'вата':
        k += 1
    else:
        print(k+1)
print('ответ: 146')