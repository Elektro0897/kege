for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 5 == 0:
        k = str(n % 5)
        k = k[:3:-1]
        k = k[::-1]
        r = str(r + k)
    else:
        o = n % 5 * 5
        o = bin(o)[2:]
        r = str(r + o)
    if int(r, 2) >= 256:
        print(n)
        break