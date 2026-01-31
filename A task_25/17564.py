def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d):
        return min(d) + max(d)
    return 0
k = 0
for n in range(700001, 10**20):
    m = f(n)
    if m % 10 == 4:
        print(n, m)
        k += 1
        if k == 5:
            break
# 700004 350004
# 700009 41194
# 700023 233344
# 700024 350014
# 700044 350024