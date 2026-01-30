def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
x = convert((3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2025), 25)
print(x.count('0'))
#10