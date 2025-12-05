from string import printable as alf
def convert(num, sys):
    res = ''
    while num:
        res += alf[num % sys] # выдаёт тут ошибку
        num //= sys
    return res[::-1]
for x in range(100):
    num1 = convert(f'7a{x}0123', 100) # выдаёт тут ошибку
    num2 = convert(f'1ba64{x}', 100) # выдаёт тут ошибку
    num3 = convert(f'{x}98012c', 100) # выдаёт тут ошибку
    num4 = num1 - num2 + num3
    if num4 % 21 == 0:
        print(convert(num4 // 21, 6))
