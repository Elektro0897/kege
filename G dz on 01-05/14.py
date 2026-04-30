from string import *
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

x = convert(5 * 1296**2021 - 4 * 216**2022 + 3 * 36**2023 - 2 * 6**2024 - 2025, 36)

for i in printable[0:36:2]:
    x = x.replace(i, '+')
print(x.count('+'))
#1013