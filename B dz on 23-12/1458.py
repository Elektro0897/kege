from itertools import *
graf = 'аб бе еж жд дв ва га гб гд гв бд де'.split()
matr = '256 13467 2456 237 136 1235 24'.split()
print(*range(1, 8))
for i in permutations('абвгдеж'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)