from string import printable as alf
for x in alf[:]:
    for y in alf[:]:
        num1 = int(f'73{x}1{y}', 67)
        num2 = int(f'49{y}6', x)
        num = num1 + num2
        if num:
            print(num)