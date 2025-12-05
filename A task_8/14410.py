from itertools import *
k = 0
alf = sorted('солнце')
for pos, val in enumerate(product(alf, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'о' and val[0] != 'е' and val.count('ц') == 2 and pos % 2 == 0:
        k += 1
print(k)