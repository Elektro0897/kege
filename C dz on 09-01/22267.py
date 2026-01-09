def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
m_n = []
for n in range(1, 100000):
    r = convert(n, 7)
    if r[-1] == '2':
        r = r.replace('3', '*')
        r = r.replace('1', '3')
        r = r.replace('*', '1')
        r = '21' + r
    else:
        r = '1' + r[1:] + '36'
    r = int(r, 7)
    if r == 664:
        m_n.append(n)
print(min(m_n))