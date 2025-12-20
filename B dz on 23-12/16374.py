from itertools import *
k = 0
for val in product('01234567', repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in val:
            if i in '02468':
                val = val.replace(i, '-')
    if val.count('-') == 2:
        k += 1
print(k)
# ответ 319488 (неправильно)