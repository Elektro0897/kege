```
from itertools import *
s = sorted('нормалье')
k = 0
l = 0
for pos, val in enumerate(product(s, repeat=6), start=1):
    val = ''.join(val)
    if val[:4] == 'норм':
        print(pos-1)
    if val[:6] == 'ненорм':
        print(pos)
print(154816-137588)
print('ответ: 17228')
```