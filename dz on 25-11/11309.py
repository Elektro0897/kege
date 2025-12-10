from string import printable as alf
for x in alf[:27]:
    num1 = int(f'8{x}38{x}68', 27)
    num2 = int(f'37{x}3163', 27)
    num = num1 + num2
    if num % 26 == 0:
        print(x, num // 26)
print('ответ: 176999110')