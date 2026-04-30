from itertools import *
graf = 'аб бд дк ке ег гв вб вд ве ед'.split()
matr = '27 1567 67 5 246 2357 1236'.split()
print(*range(1, 8))
for i in permutations('абвгдек'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
#9