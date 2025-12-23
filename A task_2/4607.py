print('z x y w')
for x in range(2):
    for y in (0, 1):
        for z in [0, 1]:
            for w in 0, 1:
                f = ((x <= z) <= y) or not w
                if not f:
                    print(z, x, y, w)
# zxyw