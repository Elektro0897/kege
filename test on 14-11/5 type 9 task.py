for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 2 == 0:
        n = r + r[:5]
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    if r > 600:
        print(r)
        break