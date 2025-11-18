k = []
for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin(n % 3 * 3)[2:]
    r = int(r, 2)
    if r <= 170:
        k.append(r)
print(max(k))