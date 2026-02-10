def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i * i <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 1:
        d += [num]
    return d
k = 0
for n in range(6086056, 10**20):
    d = fact(n)
    if len(d) == 2 and all(str(x).count('6') == 1 for x in set(d)):
        print(n, d[-1])
        k += 1
        if k == 5:
            break