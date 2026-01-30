ans = []
for n in range(1, 1000):
    r = bin(n)[2:]
    r = r.replace('0', '00')
    r = r.replace('1', '11')
    r = int(r, 2)
    if r > 63:
        ans.append(r)
print(min(ans))
#192