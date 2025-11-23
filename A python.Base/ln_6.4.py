from math import pi

r = int(input('введите высоту: '))
h = int(input('введите радиус: '))
s = 2 * pi * r * h
S = pi * r**2
print(S * 2 + s)
