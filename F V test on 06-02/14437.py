def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if len(d) > 0:
        m = sum(d) // len(d)
        if str(m)[-3:] == '313':
            return m
    return 0

k = 0
for n in range(0, 700000)[::-1]:
    if m := f(n):
        print(n, m)
        k += 1
        if k == 7:
            break