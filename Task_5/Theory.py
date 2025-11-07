# системы счисления

# двоичная система
n = 25
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'
print(bin(n)[2:])
# f'' - форматируемая строка, которая позволяет вставлять в себя переменные
print(f'{n:b}')

# восьмеричная система
print(oct(n)[2:])
print(f'{n:o}')

# шестнадцатеричная система
print(hex(n)[2:])
print(f'{n:x}')

# перевод в любую систему (2<= sys <= 9)
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]
print(convert(25, 3))

#ZZZZZZZZZZZZZZZZZZZZZOOOOOOOOOOOOOOOOOOOOOOOOOOOVVVVVVVVVVVVVVVVVVVVVVVVVV
# перевод в любую систему (2<= sys <= 36)
from string import printable as alpha
def convert2(num, sys):
    res = ''
    while num != 0:
        res += alpha[num % sys]
        num //= sys
    return res[::-1]


# перевод в десятичную сс (систему исчисления)
num_bin = '101'
num_three = '121'
num_hex = 'fa8'
print(int(num_bin, 2))
print(int(num_three, 3))
print(int(num_hex, 16))