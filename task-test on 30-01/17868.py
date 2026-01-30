from string import printable as alf
for x in alf[:19]:
    num1 = int(f'98897{x}21', 19)
    num2 = int(f'2{x}923', 19)
    num = num1 + num2
    if num % 18 == 0:
        print(x, num // 18)