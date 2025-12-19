from itertools import *
graf = 'gd df fa ab bc ce eg de ca'.split()
matr = '346 45 16 125 247 137 56'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
