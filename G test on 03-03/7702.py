from string import printable
k = set()
for x in printable[:18]:
    for y in printable[9:18]:
        num1 = int(f'5{x}{y}a', 18)
        if x < y:
            num2 = int(f'18{x}7', int(y, 18))
            num = num1 + num2
            k |= {num}
print(len(k))