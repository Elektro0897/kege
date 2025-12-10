def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
# for x in range(100):
#     num1 = convert(f'7a{x}0123', 100) # выдаёт тут ошибку
#     num2 = convert(f'1ba64{x}', 100) # выдаёт тут ошибку
#     num3 = convert(f'{x}98012c', 100) # выдаёт тут ошибку
#     num4 = num1 - num2 + num3
#     if num4 % 21 == 0:
#         print(convert(num4 // 21, 6))

for x in range(1, 100):
    num1 = 7*100**6 + 10*100**5 + x*100**4 + 0*100**3 + 1*100**2 + 2*100 + 3
    num2 = 1*100**5 + 11*100**4 + 10*100**3 + 6*100**2 + 4*100 + x
    num3 = x*100**6 + 9*100**5 + 8*100**4 + 0*100**3 + 1*100**2 + 2*100 + 12
    num4 = num1 + num2 + num3
    if num4 % 21 == 0:
        print(convert(x, 6))
print('ответ: 234')