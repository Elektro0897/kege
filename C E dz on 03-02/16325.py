from string import printable as alf
from sys import set_int_max_str_digits
set_int_max_str_digits(10000)
def convert(num, sys):
    res = ''
    while num:
        res += alf[num % sys]
        num //= sys
    return res[::-1]
x = str(map(int, str(2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024)))
for i in alf[10:27]:
    x = x.replace(i, '+')
print(x.count('+'))
#9