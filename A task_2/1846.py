print('c d b a')
for a in range(2):
    for b in (0, 1):
        for c in [0, 1]:
            for d in 0, 1:
                f = (not a and not b) or (b == c) or d
                if not f:
                    print(c, d, b, a)