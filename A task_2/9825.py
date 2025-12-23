print('z w y x')
for x in range(2):
    for y in (0, 1):
        for z in [0, 1]:
            for w in 0, 1:
                f = (x <= (z == w)) or not(y <= w)
                if not f:
                    print(z, w, y, x)
