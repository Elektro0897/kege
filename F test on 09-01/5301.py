from itertools import *
s = sorted('леся ')
k = 0
for val in product(s, repeat=5):
    val = ''.join(val)
    val = val.replace('е', '*')
    val = val.replace('я', '*')
    val = val.replace('л', '+')
    val = val.replace('с', '+')
    if '**' not in val and '++' not in val and (val[2] == ' ' or val[1] == ' ' or val[3] == ' ') and val.count(' ') == 1:
        k += 1
print(k)
