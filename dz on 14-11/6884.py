for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '1'
    else:
        r = '11' + r + '11'
    if int(r, 2) >= 255:
        print(int(r, 2))
        break
print('ответ: 255')