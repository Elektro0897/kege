k = 0
for n in range(1, 100000):
    r = hex(n)[2:]
    if r.count('b') % 2 == 0:
        r = '1' + r
    else:
        r = r + '1'
    r = int(r, 16)
    if r // 100 == 0 and r % 100 > 9:
        if 10 <= r <= 99:
            if len(str(r)) == 2:
                k += 1
print(k)