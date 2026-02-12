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

def f(num):
    d = set()
    for i in range(1, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) % 90 == 0:
        return 1
    return 0

k = 0
for n in range(5200001, 10**20):
    d = fact(n)
    if len(d) == 9 and f(n):
        print(n, d[-1])
        k += 1
        if k == 5:
            break