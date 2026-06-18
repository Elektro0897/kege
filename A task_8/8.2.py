from itertools import product

alph = sorted('АКЦЕНТ')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in 'АЕК' and val.count('Т') >= 1:
        print(pos)
        break