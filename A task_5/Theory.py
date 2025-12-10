# системы счисления

# двоичная система
# n = 25
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'
# print(bin(n)[2:])
# f'' - форматируемая строка, которая позволяет вставлять в себя переменные
# print(f'{n:b}')

# восьмеричная система
# print(oct(n)[2:])
# print(f'{n:o}')

# шестнадцатеричная система
# print(hex(n)[2:])
# print(f'{n:x}')

# перевод в любую систему (2<= sys <= 9)
# def convert(num, sys):
#     res = ''
#     while num != 0:
#         res += str(num % sys)
#         num //= sys
#     return res[::-1]
# print(convert(25, 3))

#ZZZZZZZZZZZZZZZZZZZZZOOOOOOOOOOOOOOOOOOOOOOOOOOOVVVVVVVVVVVVVVVVVVVVVVVVVV
# перевод в любую систему (2<= sys <= 36)
# from string import printable as alpha
# def convert2(num, sys):
#     res = ''
#     while num != 0:
#         res += alpha[num % sys]
#         num //= sys
#     return res[::-1]


# перевод в десятичную сс (систему исчисления)
#num_bin = '101'
#num_three = '121'
#num_hex = 'fa8'
#print(int(num_bin, 2))
#print(int(num_three, 3))
#print(int(num_hex, 16))

# Срезы
#data = '123456789'
# извлечение первых двух символов
#print(data[:2])
# извлечение без первых двух символов
#print(data[2:])
# извлечение последних двух символов
#print(data[-2:])
# извлечение без последних двух символов
#print(data[:-2])

# сумма цифр числа
# двоичная система
# num1 = '1010'
# sum1 = num1.count('1')
#print(sum1)
# любая система до 10 вкл
# num2 = '192'
# sum2 = sum(map(int, num2))
# print(sum2)

# любая система до 36 вкл
# num3 = 'ZOV'
# sum3 = sum(map(lambda z: int(z, 36), num3))
# print(sum3)