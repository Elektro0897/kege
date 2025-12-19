from itertools import *
graf = 'fe ed dg ga ah hf bf bh bc cg'.split()
matr = '478 38 256 15 34 37 168 127'.split()
print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
print('ответ:', str(34 + 11))