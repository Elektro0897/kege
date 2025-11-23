from random import random
num1 = random()
num1 = int(num1 * 10000)
num2 = num1 // 1000
num3 = num1 % 1000 // 100
num4 = num1 % 100 // 10
num5 = num1 % 10
print(num2, num3, num4, num5)