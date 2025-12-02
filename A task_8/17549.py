from itertools import *
alf = sorted('фокус') # покус, бля
for pos, val in enumerate(product(alf, repeat=5), start=1):
    val = ''.join(val)
    if val.count('ф') == 0 and val.count('у') == 2:
        print(pos)
