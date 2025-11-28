for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + bin(bin(n).count('1'))[2:]
    else:
        r = '1' + r + '101'
        print(n)
        break