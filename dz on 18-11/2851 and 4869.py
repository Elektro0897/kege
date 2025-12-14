ch = 0
nech = 0
module = 0
for n in range(2, 100000):
    r = bin(n)[2:]
    ch = r[1::2].count('1')
    nech = r[::2].count('0')
    module = abs(ch - nech)
    if module == 5:
        print(n)
        break