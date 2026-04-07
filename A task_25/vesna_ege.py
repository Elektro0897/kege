def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    for i in sorted(d):
        if i % 100 == 11 and i != 11:
            return i
    return 0
k = 0
for n in range(1350051, 10**10):
    if m := f(n):
        print(n, m)
        k += 1
        if k == 5:
            break