from math import prod
def f(num):
    d = set()
    for i in range(1, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if sum(d) % 2 != 0 and prod(d) % 2 != 0:
        if len(d) > 10:
            return len(d)
    return 0
k = 0
for n in range(800001, 10**20):
    if m := f(n):
        print(n, m)
        k += 1
        if k == 6:
            break
# 804609 27
# 815409 27
# 826281 15
# 837225 27
# 855625 15
# 859329 15
