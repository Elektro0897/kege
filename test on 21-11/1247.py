x = 729**8 - 3**18 + 85
k = 0
while x:
    if x % 9 == 0:
        k += 1
    x //= 9
print(k)