from itertools import *
graf = 'ce eg gf fa ac cd dh he ab bf'.split()
matr = '68 47 45 237 368 15 248 157'.split()
print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
        # ответ 18