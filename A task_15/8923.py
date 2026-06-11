def DEL(n, m):
    return n % m == 0
def f(x):
    p = 2508 <= x <= 2570
    return DEL(x, a) or (p <= (not DEL(x, 214) or (x + a <= 5286)))
for a in range(1, 3000)[::-1]:
    if all(f(x) for x in range(1, 3000)):
        print(a)
        break