def f(x, y):
    return (x + y <= 30) or (y <= x + 2) or (y >= a)
for a in range(0, 500)[::-1]:
    if all(f(x, y) for x in range(1, 500) for y in range(1, 500)):
        print(a)
        break
        #17