from itertools import *
from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
k = 0
for n in product(printable[:16], repeat=5):
    if n.count('6') == 2 and n[0] != '0':
        for i in printable[:6:2]: # 0 2 4
            n = str(n).replace(i, '+')
        for i in printable[8:16:2]: # 8 10 12
            n = n.replace(i, '+')
        if '+6' not in n and '6+' not in n and '66' not in n:
            k += 1
print(k)