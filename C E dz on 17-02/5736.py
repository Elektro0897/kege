def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 1:
        if max(d) % 7 == 0:
            return max(d)
    return 0
k = 0
for n in range(10**9 + 1, 10**20):
    if str(n) == str(n)[::-1]:
        if m := f(n):
            print(n, m)
            k += 1
            if k == 5:
                break