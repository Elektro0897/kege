num = 17 * 125**453 + 117 * 5**231 - 3*5**13 - 2357
k = 0
while num:
    if num % 125 <= 37: k += 1
    num //= 125
print(k)