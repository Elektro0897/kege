from fnmatch import fnmatch
for n in range(124065 - 124065 % 161, 10**8 + 1, 161):
    if fnmatch(str(n), '12*4?65'):
        print(n, n // 161)

print('#################')

from itertools import *
from string import printable as alf
# 100000000
# 12*4?65
ans = []
for v in alf[:10]:
    for l in range(0, 3):
        for z in product(alf[:10], repeat=l):
            num = int(f'12{''.join(z)}4{v}65')
            if num % 161 == 0 and num <= 10**8:
                ans.append([num, num // 161])
for i in sorted(ans):
    print(*i)