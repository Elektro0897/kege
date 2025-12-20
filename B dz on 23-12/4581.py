from itertools import *
graf = 'ad de eg gc cf fa ba be bf'.split()
matr = '37 367 125 56 34 247 126'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
        # ответ 66