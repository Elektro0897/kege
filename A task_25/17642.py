def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    for i in sorted(d):
        if i % 10 == 9 and i != 9:
            return i
    return 0
k = 0
for n in range(800001, 10**20):
    m = f(n)
    if m:
        print(n, m)
        k += 1
        if k == 5:
            break