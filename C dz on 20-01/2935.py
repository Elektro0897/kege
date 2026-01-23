def f(x, y):
    return (2 * y + 3 * x != 135) or (y > a) or (x > a)
for a in range(-1000, 1000)[::-1]:
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
        #26