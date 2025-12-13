from itertools import *
k = 0
for val in product('полина', repeat=8):
    val = ''.join(val)
    val = val.replace('о', '*')
    val = val.replace('и', '*')
    val = val.replace('а', '*')
    val = val.replace('п', '+')
    val = val.replace('л', '+')
    val = val.replace('н', '+')
    if val.count('+') > val.count('*'):
        k += 1
print(k)