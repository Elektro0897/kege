def f(num):
    s = 0
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 1:
        for l in d:
            s += int(d[l])
            if s[-2:-1] == '23':
                return s
    return 0

for n in range(1000, 10000):
    if m := f(n):
        print(m, n)