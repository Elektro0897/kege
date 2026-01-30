from itertools import *
s = sorted('аекнс')
for pos, val in enumerate(product(s, repeat=6), start=1):
    val = ''.join(val)
    if val == 'сенека':
        print(pos)
        #13536