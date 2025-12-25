print('y z x w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x <= y) and z and not w
                if f:
                    print(y, z, x, w)
                    #yzxw