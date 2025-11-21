from string import printable as alf
for x in alf[:23]:
    num1 = int(f'7{x}38596', 23)
    num2 = int(f'14{x}36', 23)
    num3 = int(f'61{x}7', 23)
    num = num1 + num2 + num3
    if num % 22 == 0:
        print(x, num // 22)
print('ответ: 47163321')