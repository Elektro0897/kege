num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if abs(num1 - num3) == 1 and abs(num2 - num4) == 2 or abs(num2 - num4) == 1 and abs(num1 - num3) == 2:
    print('может')
else:
    print('не может')