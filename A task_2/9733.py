print('y x w z')
for x in range(2):
    for y in (0, 1):
        for z in [0, 1]:
            for w in 0, 1:
                f = (x and not y) or (x == z) or w
                if not f:
                    print(y, x, w, z)
# yxwz