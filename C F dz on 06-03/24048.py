from string import printable
for p in printable[33:36]:
    num1 = int(f'kot', int(p, 36))
    num2 = int(f'golodni', int(p, 36))
    num3 = int(f'meeow', int(p, 36))
    num4 = int(f'100', int(p, 36))
    if num1 + num2 == num3 * num4 - 20194023088:
        print(int(f'purr', int(p, 36)))