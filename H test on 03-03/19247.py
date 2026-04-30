def f(x, y):
    return (x - 3 * y < a) or (y > 400) or (x > 56)
ans = []
for a in range(0, 300):
    if all(f(x, y) for x in range(1, 300) for y in range(1, 300)):
        print(a)
        break