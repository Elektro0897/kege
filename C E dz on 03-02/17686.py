def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    for i in sorted(d):
        if i % 10 == 7 and i != 7:
            return i
    return 0
k = 0
for n in range(700001, 10**20):
    m = f(n)
    if m:
        print(n, m)
        k += 1
        if k == 5:
            break
# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167