k = ''
for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    if r < 30:
        k = n
print(k)