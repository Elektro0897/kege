ans = []
for x in range(10, 14):
    for y in range(10, 14):
        num1 = int(f'7{x}37', 14)
        num2 = int(f'9{y}63', x)
        num3 = int(f'15148', y)
        num = num1 + num2 - num3
        ans.append(num // (x + y))
print(max(ans))
#22455