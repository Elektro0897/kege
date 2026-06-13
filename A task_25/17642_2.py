def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    for i in sorted(d):
        if i % 10 == 9 and i != 9:
            return i
    return 0
k = 0
for n in range(800000 + 1, 10**10):
    if m := f(n):
        print(n, m)
        k += 1
        if k == 5:
            break
# 800001 309
# 800003 47059
# 800004 409
# 800006 269
# 800007 39