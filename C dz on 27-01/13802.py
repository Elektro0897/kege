from itertools import *
graf = 'ae eh hg gc cf fa de db df bh bg'.split()
matr = '367 568 18 58 247 127 156 234'.split()
print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
        print('ответ:', 10+11)