print('z y  w x')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((w <= y) <= x) or not z
                if not f:
                    print(z, y, w, x)
                    #zywx