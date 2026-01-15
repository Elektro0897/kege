def DEL(n, m):
    return n % m == 0
def f(x):
    return DEL(x, 128) <= ((not DEL(x, a)) <= (not DEL(x, 80)))
for a in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
        #640