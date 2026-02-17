def f(n):
    for x in range(113, n, 226):
        for i in range(0, 13):
            if x + 3 ** i == n:
                return i
    return 0
k = 0
for n in range(100000, 1000000, 2):
    if '0' not in str(n) and (m := f(n)):
        print(n, m)
        k += 1
        if k == 5:
            break