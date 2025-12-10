from string import printable as alf
def convert(num, sys):
    res = ''
    while num != 0:
        res += alf[num % sys]
        num //= sys
    return res[::-1]
x = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
r = convert(x, 25)
print(r.count('0'))
print('ответ: 10')