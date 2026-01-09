print('z y x w')
for x in range(2):
    for y in range(2):
        for z in range(2):
             for w in range(2):
                 f = (z <= (not (y <= x))) or w
                 if not f:
                     print(z, y, x, w)
                     #zyxw