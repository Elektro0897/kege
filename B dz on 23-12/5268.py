from itertools import *
k = 0
for val in permutations('амфибрахий'):
    val = ''.join(val)
    if 'аафии' in val or 'иифаа' in val:
        k += 1
print(k)
# ответ 5760 (неправильно)