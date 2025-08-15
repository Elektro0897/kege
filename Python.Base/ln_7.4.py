from random import randint
num1 = randint(100, 999)
print(num1)
num2 = num1 % 10
num3 = num1 % 100 // 10
num4 = num1 // 100
if num2 == 1 or num2 == 3 or num2 == 5 or num2 == 7:
    print(num2)
elif num3 == 1 or num3 == 3 or num3 == 5 or num3 == 7:
    print(num3)
elif num4 == 1 or num4 == 3 or num4 == 5 or num4 == 7:
    print(num4)
else:
    print('хрень, передлывай')
