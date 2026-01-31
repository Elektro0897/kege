def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d):
        return min(d) + max(d)
    return 0
k = 0
for n in range(800001, 10**10):
    m = f(n)
    if m % 10 == 4:
        print(n, m)
        k += 1
        if k == 5:
            break
# 800004 400004
# 800009 114294
# 800013 266674
# 800024 400014
# 800033 61554