for n in range(1, 100000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '11' + r[2:] + '1'
    else:
        if r.count('0') < r.count('1'):
            r = r + '0'
        else:
            r = r + '1'
    if int(r, 2) > 271:
        print(n)
        break
print('ответ: 129')