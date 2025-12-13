from itertools import *
k = 0
for val in product('01234567', repeat=9):
    val = ''.join(val)
    val = val.replace('0', '*')
    val = val.replace('2', '*')
    val = val.replace('4', '*')
    val = val.replace('6', '*')
    if val.count('7') == 5 and '*7*' not in val and '*7' not in val and '7*' not in val:
        k += 1
print(k)