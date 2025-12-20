from itertools import *
graf = 'аб бв вд де ек кг гв ва ге ве'.split()
matr = '24 146 56 1267 36 23457 46'.split()
print(*range(1,8))
for i in permutations('абвгдек'):
    if all(str(i.index(x) + 1) in matr[i.index(y)] for x, y in graf):
        print(*i)
        # ответ 30