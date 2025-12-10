t = 0
for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 8 == 0:
        r = r + r[-2:]
    else:
        t = bin(n % 8 * 2)[2:]
        r = r + t
    r = int(r, 2)
    if r > 3000:
        print(n)
        break
print('ответ: 188')