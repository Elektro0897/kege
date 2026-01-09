from string import printable as alf
import itertools
k =[]
for x in alf[:15]:
    m = int(f'432{x}3', 15)
    n = int(f'86{x}86', 15)
    for a in itertools.count(1):
        b = m + a
        if b % n == 0:
            k.append(a)
            break
print(min(k))