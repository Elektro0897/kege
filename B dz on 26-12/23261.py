print('y x w z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not(w <= (x == y)) and (z <= x)
                if f:
                    print(y, x, w, z)
                    #yxwz