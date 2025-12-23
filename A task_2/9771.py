print('w x y z')
for x in range(2):
    for y in (0, 1):
        for z in [0, 1]:
            for w in 0, 1:
                f = (y <= x) and not z and w
                if f:
                    print(w, x, y, z)
# wxyz