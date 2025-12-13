from itertools import *
k = 0
for val in product('дионсй', repeat=6):
    val = ''.join(val)
    val = val.replace('д', '*')
    val = val.replace('н', '*')
    if val.count('*') >= 1 and 'ии' not in val and 'дд' not in val and 'нн' not in val and 'оо' not in val and 'сс' not in val and 'йй' not in val:
        k += 1
print(k)