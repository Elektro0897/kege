from string import printable as alf
k = 0
for x in alf[:29]:
    num1 = int(f'923{x}874', 29)
    num2 = int(f'524{x}6152', 29)
    num = num1 + num2
    if  num % 28 == 0:
        k = num // 28
print(k)